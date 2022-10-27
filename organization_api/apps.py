from django.apps import AppConfig


class OrganizationApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'organization_api'

    def ready(self):
        import organization_api.signals
