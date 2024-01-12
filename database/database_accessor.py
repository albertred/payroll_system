from decimal import Decimal
from database.models import Payperiod, Employee
import datetime
from datetime import datetime
from django.db.models import Max


def retrieve_max_pay_period():
    return Payperiod.objects.aggregate(Max('pay_period_number'))['pay_period_number__max']


def read_pay_period_list_by_employ_id(employee_id):
    print('>>>>>>>>>> ' + str(employee_id))
    list_of_pay_period = Payperiod.objects.filter(employee_id=employee_id)
    print('>>>>>>>>>> ' + str(len(list_of_pay_period)))
    return list_of_pay_period


def retrieve_employee_info_from_db(employee_id):
    return Employee.objects.get(employee_id=employee_id)


def save(pay_period_info):
    model = Payperiod()
    model.employee_id = pay_period_info.employee_id
    model.CPP_ytd = pay_period_info.CPP_ytd

    model.pay_period_number = pay_period_info.pay_period_number
    model.pay_period_start = pay_period_info.pay_period_start
    model.pay_period_end = pay_period_info.pay_period_end
    model.pay_date = pay_period_info.pay_date
    model.regular_rate = pay_period_info.regular_rate
    model.vacation_pay = pay_period_info.vacation_pay
    model.YTD_vacation = pay_period_info.YTD_vacation
    print(type(pay_period_info.holiday_hours))
    print(type(pay_period_info.holiday_hours.item()))
    model.holiday_hours = Decimal.from_float(pay_period_info.holiday_hours.item())
    model.YTD_payroll = pay_period_info.YTD_payroll
    model.regular_current_total = pay_period_info.regular_current_total
    model.regular_hours = Decimal.from_float(pay_period_info.regular_hours.item())
    model.overtime_rate = Decimal.from_float(pay_period_info.overtime_rate.item())
    model.overtime_hours = Decimal.from_float(pay_period_info.overtime_hours.item())
    model.overtime_current_total = Decimal.from_float(pay_period_info.overtime_current_total.item())
    model.El_ytd = Decimal.from_float(pay_period_info.El_ytd.item())
    model.El_current_pay_period = Decimal.from_float(pay_period_info.El_current_pay_period)
    model.income_tax_ytd = Decimal.from_float(pay_period_info.income_tax_ytd)
    model.income_tax_current_pay_period = Decimal.from_float(pay_period_info.income_tax_current_pay_period)
    model.benefits_current_pay_period = Decimal.from_float(pay_period_info.benefits_current_pay_period)
    model.benefits_ytd = Decimal.from_float(pay_period_info.benefits_ytd)
    model.gross_total = Decimal.from_float(pay_period_info.gross_total)
    model.deductions = Decimal.from_float(pay_period_info.deductions)
    model.net_pay = Decimal.from_float(pay_period_info.net_pay)

    model.CPP_current_pay_period = pay_period_info.CPP_current_pay_period

    model.OFFOT_time_rate = Decimal.from_float(pay_period_info.OFFOT_time_rate.item())
    model.OFFOT_time_hours = Decimal.from_float(pay_period_info.OFFOT_time_hours.item())
    model.OFFOT_time_current_total = Decimal.from_float(pay_period_info.OFFOT_time_current_total.item())

    model.CPP_current_pay_period = Decimal.from_float(pay_period_info.CPP_current_pay_period.item())
    model.CPP_ytd = Decimal.from_float(pay_period_info.CPP_ytd.item())

    model.YTD_payroll = pay_period_info.YTD_payroll
    model.YTD_deductions = pay_period_info.YTD_deductions
    model.YTD_net_pay = pay_period_info.YTD_net_pay

    model.save()

