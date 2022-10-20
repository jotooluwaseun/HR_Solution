from django.contrib import admin
from .models import (
    Employee, Country, Status, Grade, Unit, Department,
    Address, NOKAddress, NOK, Education, PreviousWorkExperience
)

admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(Status)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Address)
admin.site.register(NOK)
admin.site.register(NOKAddress)
admin.site.register(Education)
admin.site.register(PreviousWorkExperience)
