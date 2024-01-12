import datetime


class PayPeriodInfo:
    employee_id = 0
    pay_period_number = 0
    pay_period_start = datetime.datetime.now()
    pay_period_end = datetime.datetime.now()
    pay_date = datetime.datetime.now()
    regular_rate = 0

    OFFOT_time_rate = 0.0
    OFFOT_time_hours = 0.0
    OFFOT_time_current_total = 0.0

    overtime_rate = 0
    vacation_pay = 0
    regular_hours = 0

    overtime_hours = 0
    holiday_hours = 0
    current_total = 0

    El_current_pay_period = 0
    income_tax_current_pay_period = 0
    benefits_current_pay_period = 0
    El_ytd = 0
    income_tax_ytd = 0
    benefits_ytd = 0
    YTD_payroll = 0
    YTD_vacation = 0
    YTD_deductions = 0
    YTD_net_pay = 0
    gross_total = 0
    deductions = 0
    net_pay = 0
    regular_current_total = 0
    overtime_current_total = 0

    CPP_current_pay_period = 0.0
    CPP_ytd = 0

    def __str__(self):
        return self.employee_id