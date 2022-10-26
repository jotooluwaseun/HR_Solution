from django.urls import path
from organization_api.views import (
    CountryList, CountryDetails,
    CompanyList, CompanyDetails
)

app_name = 'organization_api'

urlpatterns = [
    path('country/', CountryList.as_view(), name='country-list'),
    path('country/<int:pk>/', CountryDetails.as_view(), name='country-details'),

    path('company/', CompanyList.as_view(), name='company-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
]
