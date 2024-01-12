import datetime
import re
from datetime import timedelta

def calculate(pay_period_info, list_of_pay_period):
    pay_period_info.YTD_net_pay = 100.00

    sort(list_of_pay_period)

    pay_period_info.CPP_ytd = pay_period_info.CPP_current_pay_period
    pay_period_info.YTD_vacation = pay_period_info.vacation_pay

    pay_period_info.OFFOT_time_current_total = pay_period_info.OFFOT_time_hours * pay_period_info.OFFOT_time_rate
    pay_period_info.regular_current_total = pay_period_info.regular_hours * pay_period_info.regular_rate
    pay_period_info.overtime_current_total = pay_period_info.overtime_hours * pay_period_info.overtime_rate
    pay_period_info.gross_total = pay_period_info.regular_current_total + pay_period_info.OFFOT_time_current_total + \
                                  pay_period_info.overtime_current_total + pay_period_info.vacation_pay
    pay_period_info.deductions = pay_period_info.CPP_current_pay_period + pay_period_info.El_current_pay_period + \
                                pay_period_info.income_tax_current_pay_period + pay_period_info.benefits_current_pay_period
    pay_period_info.net_pay = pay_period_info.gross_total - pay_period_info.deductions

    pay_period_info.CPP_ytd = pay_period_info.CPP_current_pay_period
    pay_period_info.El_ytd = pay_period_info.El_current_pay_period
    pay_period_info.income_tax_ytd = pay_period_info.income_tax_current_pay_period
    pay_period_info.benefits_ytd = pay_period_info.benefits_current_pay_period

    pay_period_info.YTD_payroll = pay_period_info.gross_total
    pay_period_info.YTD_deductions = pay_period_info.deductions
    pay_period_info.YTD_net_pay = pay_period_info.net_pay

    pay_period_info.pay_date = pay_period_info.pay_period_end + timedelta(days=7)

    for x in list_of_pay_period:
        pay_period_info.YTD_vacation = pay_period_info.YTD_vacation + float(x.vacation_pay)
        pay_period_info.CPP_ytd = pay_period_info.CPP_ytd + float(x.CPP_current_pay_period)
        pay_period_info.El_ytd = pay_period_info.El_ytd + float(x.El_current_pay_period)
        pay_period_info.income_tax_ytd = pay_period_info.income_tax_ytd + float(x.income_tax_current_pay_period)
        pay_period_info.benefits_ytd = pay_period_info.benefits_ytd + float(x.benefits_current_pay_period)
        pay_period_info.YTD_payroll = pay_period_info.YTD_payroll + float(x.gross_total)
        pay_period_info.YTD_deductions = pay_period_info.YTD_deductions + float(x.deductions)
        pay_period_info.YTD_net_pay = pay_period_info.YTD_net_pay + float(x.net_pay)



    return pay_period_info


def get_pay_period_number(pay_period_record):
    return pay_period_record.pay_period_number


def sort(list_of_pay_period):
    list_of_pay_period.sort(key=get_pay_period_number)
    return list_of_pay_period
