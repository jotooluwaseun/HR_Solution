from rest_framework import serializers
from organization_api.models import Country, Company, Status


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    location = CountrySerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'size', 'location')


class GetAllCompanySerializer(serializers.ModelSerializer):
    location = CountryNameSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ('name', 'size', 'location')
