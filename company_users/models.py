from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, company_email, company_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(company_email, company_name, password, **other_fields)

    def create_user(self, company_email, company_name, password, **other_fields):

        if not company_email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(company_email)
        user = self.model(company_email=company_email, company_name=company_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class CompanyUser(AbstractBaseUser, PermissionsMixin):

    company_email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'company_email'
    REQUIRED_FIELDS = ['company_name']

    def __str__(self):
        return self.company_name
