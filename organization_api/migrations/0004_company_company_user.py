# Generated by Django 4.1.2 on 2022-10-26 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization_api', '0003_employee_manual_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='company_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
