from rest_framework import serializers
from organization_api.models import Country, Company, Status
from django.contrib.auth import get_user_model

User = get_user_model()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    location = CountryNameSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Company
        exclude = ('id', 'company_user',)


class UpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_number', 'name', 'size', 'location', 'status')
        read_only_fields = ('company_number',)


class GetAllCompanySerializer(serializers.ModelSerializer):
    location = CountryNameSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ('name', 'size', 'location')


class CreateUserAndCompanySerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['company_email', 'company_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            company_email=self.validated_data['company_email'],
            company_name=self.validated_data['company_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'company_name', 'company_email')
