from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from organization.models import Country, Company, CompanyNumber
from organization.serializers import CountrySerializer, CompanySerializer, CreateCompanySerializer


# -----------------------------------------------------
# Get all the country names and their associated dialing codes
@api_view(['GET'])
def country_list(request):
    country = Country.objects.all()
    serializer = CountrySerializer(country, many=True)
    return Response(serializer.data)


# -----------------------------------------------------
# Get individual country names and their associated dialing codes
@api_view(['GET'])
def country_details(request, id):
    country = Country.objects.get(dailing_code=id)
    serializer = CountrySerializer(country)
    return Response(serializer.data)


# -----------------------------------------------------
# Get all the companies and also create a new company
@api_view(['GET'])
def retrieve_company(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_company(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CreateCompanySerializer(company, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateCompanySerializer(data=request.data)
        if serializer.is_valid():
            company_number = 'J' + str(company_number_generator())
            serializer.save(company_number=company_number)
            content = {'Successfully Created!'}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = {'Something went wrong. Please try again!'}
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------
# Retrieve and update individual company details
@api_view(['GET', 'PUT'])
def retrieve_update_company(request, pk):
    if request.method == 'GET':
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'Successfully Updated!'}
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {'Something went wrong. Please try again!'}
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def company_number_generator():
    last_number = CompanyNumber.objects.all()
    for number in last_number:
        company_number = number.last_number
        number.last_number = number.last_number + 1
        number.save()
        return company_number
