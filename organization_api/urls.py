from django.urls import path
from organization_api.views import (
    CountryListView, CountryDetailsView,
    CompanyListView, CompanyDetailsView, CreateUserAndCompanyView,
    LoginView, UserView, LogoutView
)

app_name = 'organization_api'

urlpatterns = [
    path('country/', CountryListView.as_view(), name='country-list'),
    path('country/<int:pk>/', CountryDetailsView.as_view(), name='country-details'),

    path('company/', CompanyListView.as_view(), name='company-list'),
    path('company/<str:company_number>/', CompanyDetailsView.as_view(), name='company-details'),
    path('registration/create-company/', CreateUserAndCompanyView.as_view(), name='create-company'),

    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
