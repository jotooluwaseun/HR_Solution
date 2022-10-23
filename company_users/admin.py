from django.contrib import admin
from .models import CompanyUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = CompanyUser
    search_fields = ('company_email', 'company_name',)
    list_filter = ('company_email', 'company_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('company_email', 'company_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('company_email', 'company_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        CompanyUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_email', 'company_name', 'password1', 'password2', 'is_active',
                       'is_staff')}
         ),
    )


admin.site.register(CompanyUser, UserAdminConfig)
