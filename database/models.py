from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=50)
    employee_email = models.EmailField(max_length=254)


class Payperiod(models.Model):
    employee_id = models.CharField(max_length=50)
    pay_period_number = models.IntegerField()
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    pay_date = models.DateField()
    regular_rate = models.DecimalField(max_digits=10, decimal_places=2)

    OFFOT_time_rate = models.DecimalField(max_digits=10, decimal_places=2)
    OFFOT_time_hours = models.DecimalField(max_digits=6, decimal_places=2)
    OFFOT_time_current_total = models.DecimalField(max_digits=12, decimal_places=2)

    overtime_rate = models.DecimalField(max_digits=10, decimal_places=2)
    vacation_pay = models.DecimalField(max_digits=12, decimal_places=2)
    regular_hours = models.DecimalField(max_digits=6, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=6, decimal_places=2)
    holiday_hours = models.DecimalField(max_digits=6, decimal_places=2)
    regular_current_total = models.DecimalField(max_digits=12, decimal_places=2,)
    overtime_current_total = models.DecimalField(max_digits=12, decimal_places=2)
    El_current_pay_period = models.DecimalField(max_digits=12, decimal_places=2)
    income_tax_current_pay_period = models.DecimalField(max_digits=12, decimal_places=2)
    benefits_current_pay_period = models.DecimalField(max_digits=12, decimal_places=2)
    El_ytd = models.DecimalField(max_digits=12, decimal_places=2)
    income_tax_ytd = models.DecimalField(max_digits=12, decimal_places=2)
    benefits_ytd = models.DecimalField(max_digits=12, decimal_places=2)
    YTD_payroll = models.DecimalField(max_digits=12, decimal_places=2)
    YTD_vacation = models.DecimalField(max_digits=12, decimal_places=2)
    YTD_deductions = models.DecimalField(max_digits=12, decimal_places=2)
    YTD_net_pay = models.DecimalField(max_digits=12, decimal_places=2)
    gross_total = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2)
    net_pay = models.DecimalField(max_digits=12, decimal_places=2)

    CPP_current_pay_period = models.DecimalField(max_digits=12, decimal_places=2)
    CPP_ytd = models.DecimalField(max_digits=12, decimal_places=2)



