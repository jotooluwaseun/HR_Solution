from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from organization_api.models import Country, Company, CompanyNumber
from organization_api.serializers import (
    CountrySerializer,
    CompanySerializer, UpdateCompanySerializer, GetAllCompanySerializer,
    CreateUserAndCompanySerializer,
    UserSerializer
)
from rest_framework.permissions import DjangoModelPermissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator
import jwt, datetime

from django.contrib.auth import get_user_model

User = get_user_model()


# Country views
class CountryListView(APIView):
    def get(self, request):
        country = Country.objects.all()
        print(User)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class CountryDetailsView(APIView):
    def get(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist:
            content = {'Country cannot be found!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


# Company views
class CompanyListView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = GetAllCompanySerializer(company, many=True)
        return Response(serializer.data)


class CompanyDetailsView(APIView):
    def get(self, request, company_number):
        try:
            company = Company.objects.get(company_number=company_number)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            content = {'Company cannot be found!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=UpdateCompanySerializer)
    def put(self, request, company_number):
        try:
            company = Company.objects.get(company_number=company_number)
            serializer = UpdateCompanySerializer(instance=company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                content = {'Successfully Updated!'}
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            content = {'Something went wrong! The company you are trying to update may not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class CreateUserAndCompanyView(APIView):
    @swagger_auto_schema(request_body=CreateUserAndCompanySerializer)
    def post(self, request, format=None):
        try:
            serializer = CreateUserAndCompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                content = {'Created Successfully!'}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            content = {'Something went wrong! The company you are trying to update may not exist.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class CreateUserAndCompanyView(APIView):
    @swagger_auto_schema(request_body=CreateUserAndCompanySerializer)
    def post(self, request, format=None):
        serializer = CreateUserAndCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'Created Successfully!'}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data['company_email']
        password = request.data['password']

        user = User.objects.filter(company_email=email).first()

        if user is None:
            raise AuthenticationFailed('Company not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token}
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logged out successfully'
        }
        return response
