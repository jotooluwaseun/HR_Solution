# Generated by Django 4.1.2 on 2022-10-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]