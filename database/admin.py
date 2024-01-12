from django.contrib import admin

from .models import Employee
from .models import Payperiod

admin.site.register(Employee)
admin.site.register(Payperiod)