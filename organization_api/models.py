from django.db import models


class Employee(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    personal_email = models.EmailField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER)
    dob = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    alternative_phone_number = models.CharField(max_length=15, blank=True, null=True)
    company = models.ForeignKey('Company', blank=True, null=True, on_delete=models.SET_NULL)
    salary = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    grade = models.ForeignKey('Grade', blank=True, null=True, on_delete=models.SET_NULL)
    unit = models.ForeignKey('Unit', blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='unit')
    department = models.ForeignKey('Department', blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name='department')
    passport_number = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey('Country', blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name='nationality')
    country = models.ForeignKey('Country', blank=True, null=True, on_delete=models.SET_NULL, related_name='country')
    account_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('Status', blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.employee_id + ')'

    class Meta:
        verbose_name_plural = "Employees"


class Company(models.Model):
    SIZE = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    )
    company_number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True, choices=SIZE)
    location = models.ForeignKey('Country', blank=True, null=True, on_delete=models.SET_NULL, related_name='location')
    status = models.ForeignKey('Status', blank=True, null=True, on_delete=models.SET_NULL, default=1,
                               related_name='status')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name + ' (' + str(self.company_number) + ')'

    class Meta:
        verbose_name_plural = "Companies"


class Status(models.Model):
    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Not Active", "Not Active"),
        ("Exited", "Exited"),
        ("Suspended", "Suspended"),
        ("Retired", "Retired"),
        ("Deleted", "Deleted"),
    )
    name = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Status"
        ordering = ["id"]


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    dailing_code = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']


class Grade(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.company

    class Meta:
        verbose_name_plural = "Grades"


class Unit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    head = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL, related_name="unit_head")
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.company

    class Meta:
        verbose_name_plural = "Units"


class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    head = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL, related_name="department_head")
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.company

    class Meta:
        verbose_name_plural = "Departments"


class Address(models.Model):
    ADDRESS_TYPE = (
        ("Address 1", "Address 1"),
        ("Address 2", "Address 2"),
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    address_type = models.CharField(max_length=50, blank=True, null=True, choices=ADDRESS_TYPE)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.address + " - " + self.employee

    class Meta:
        verbose_name_plural = "Addresses"


class NOK(models.Model):
    RELATIONSHIP = (
        ("Spouse", "Spouse"),
        ("Son", "Son"),
        ("Daughter", "Daughter"),
        ("Sibling", "Sibling"),
        ("Parent", "Parent"),
        ("Guardian", "Guardian"),
        ("Other", "Other"),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.CharField(max_length=255, blank=True, null=True, choices=RELATIONSHIP)
    Other_relationship = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name + " - " + self.employee

    class Meta:
        verbose_name_plural = "Next of Kin"


class NOKAddress(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    nok = models.ForeignKey(NOK, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.address + " - " + self.nok

    class Meta:
        verbose_name_plural = "NOK Address"


class Education(models.Model):
    school = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    course_of_study = models.CharField(max_length=255, blank=True, null=True)
    graduated_year = models.CharField(max_length=4, blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.school + ' - ' + self.employee

    class Meta:
        verbose_name_plural = "Education"


class PreviousWorkExperience(models.Model):
    company = models.CharField(max_length=255, blank=True, null=True)
    job_role = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.company + ' - ' + self.employee

    class Meta:
        verbose_name_plural = "Previous Work Experience"


class CompanyNumber(models.Model):
    last_number = models.IntegerField()

    def __str__(self):
        return 'Last Company Number: ' + str(self.last_number)

    class Meta:
        verbose_name_plural = "Company Number"
