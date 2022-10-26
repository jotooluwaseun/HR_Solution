from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from organization_api.models import Employee
from admin_management_api.serializers import (
    EmployeeSerializer
)
