from django.urls import path
from organization.views import (
    country_list, country_details, retrieve_company, create_company, retrieve_update_company,
)

urlpatterns = [
    path('country-list/', country_list, name='country-list'),
    path('country-list/<int:id>/', country_details, name='country-details'),
    path('retrieve-company/', retrieve_company, name='retrieve-company'),
    path('create-company/', create_company, name='create-company'),
    path('retrieve-update-company/<int:pk>/', retrieve_update_company, name='retrieve-update-company'),
]
