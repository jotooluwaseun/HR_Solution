from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from organization_api.models import Country, Company, CompanyNumber
from organization_api.serializers import (
    CountrySerializer,
    CompanySerializer, CreateCompanySerializer, GetAllCompanySerializer
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator


# Country views
class CountryList(APIView):
    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class CountryDetails(APIView):
    def get(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist:
            content = {'Country cannot be found!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# Company views
class CompanyList(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = GetAllCompanySerializer(company, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CreateCompanySerializer)
    def post(self, request, format=None):
        serializer = CreateCompanySerializer(data=request.data)
        if serializer.is_valid():
            company_number = 'J' + str(companyNumberGenerator())
            serializer.save(company_number=company_number)
            content = {'Successfully Created!'}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = {'Something went wrong. Please try again!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# This function automatically generates Company Numbers
def companyNumberGenerator():
    last_number = CompanyNumber.objects.all()
    for number in last_number:
        company_number = number.last_number
        number.last_number = number.last_number + 1
        number.save()
        return company_number


class CompanyDetails(APIView):
    def get(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            content = {'Company cannot be found!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CreateCompanySerializer)
    def put(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            serializer = CreateCompanySerializer(instance=company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                content = {'Successfully Updated!'}
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            content = {'Something went wrong! The company you are trying to update may not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
