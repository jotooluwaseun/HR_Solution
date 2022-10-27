from django.db.models.signals import post_save, post_delete
from organization_api.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()


# Receiving signals from senders
def createCompany(sender, instance, created, **kwargs):
    if created:
        user = instance
        company = Company.objects.create(
            company_user=user,
            name=user.company_name,
            email=user.company_email,
        )


def updateCompany(sender, instance, created, **kwargs):
    Company = instance
    user = Company.company_user

    if not created:
        user.company_name = Company.name
        user.company_email = Company.email
        user.save()


def deleteCompany(sender, instance, **kwargs):
    user = instance.company_user
    user.delete()


# Sending signals from senders
post_save.connect(createCompany, sender=User)
post_save.connect(updateCompany, sender=Company)
post_delete.connect(deleteCompany, sender=Company)
