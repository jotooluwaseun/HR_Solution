from django.urls import path
from company_users.views import CustomUserCreate, BlacklistTokenView

app_name = 'company_users'

urlpatterns = [
    path('register/', CustomUserCreate, name='create-user'),
    path('logout/blacklist/', BlacklistTokenView, name='blacklist'),
]
