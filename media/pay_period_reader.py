import pandas as pandas
import os

from database.database_accessor import read_pay_period_list_by_employ_id, retrieve_max_pay_period
from duck.excel.pay_period_info import PayPeriodInfo


def retrieve_current_pay_period_number(uploaded_file_path):
    df = pandas.read_excel(uploaded_file_path, sheet_name='Sheet1')
    return df.iloc[1]["Pay Period #"]


def check_consecutive(max_pay_period_number, current_pay_period_number):
    print(max_pay_period_number)
    print(type(max_pay_period_number))
    print(current_pay_period_number)
    print(type(current_pay_period_number))
    if max_pay_period_number is None:
        return current_pay_period_number == 1
    else:
        return current_pay_period_number == max_pay_period_number + 1


def validate_excel(uploaded_file_path):
    max_pay_period_number = retrieve_max_pay_period()
    current_pay_period_number = retrieve_current_pay_period_number(uploaded_file_path)
    return check_consecutive(max_pay_period_number, current_pay_period_number)


def read_from_excel(uploaded_file_path):
    df = pandas.read_excel(uploaded_file_path, sheet_name='Sheet1')

    pay_period_info_list = []

    # TODO: figure out how to get the total number of rows in Excel using pandas API/function?
    total_num_of_rows = df.shape[0]
    print('total number of rows is: ' + str(total_num_of_rows))

    for x in range(total_num_of_rows):
        pay_period_info = PayPeriodInfo()

        if df.iloc[x]["Employee ID"] == float('NaN'):
            continue

        pay_period_info.employee_id = df.iloc[x]["Employee ID"]

        print('first cell of row ' + str(x) + ' is: [' + str(pay_period_info.employee_id) + ']')

        pay_period_info.pay_period_number = df.iloc[x]["Pay Period #"]
        pay_period_info.pay_period_start = df.iloc[x]["Pay Period Start"]
        pay_period_info.pay_period_end = df.iloc[x]["Pay Period End"]
        pay_period_info.CPP_current_pay_period = df.iloc[x]["CPP Current Pay Period"]
        pay_period_info.regular_rate = df.iloc[x]["Regular Rate"]
        pay_period_info.vacation_pay = df.iloc[x]["Vacation Pay"]
        pay_period_info.holiday_hours = df.iloc[x]["Holiday Hours"]
        pay_period_info.regular_hours = df.iloc[x]["Regular Hours"]

        pay_period_info.OFFOT_time_rate = df.iloc[x]["OFF/OT TIME Rate"]
        pay_period_info.OFFOT_time_hours = df.iloc[x]["OFF/OT Time Hours"]

        pay_period_info.overtime_rate = df.iloc[x]["Overtime Rate"]
        pay_period_info.overtime_hours = df.iloc[x]["Overtime Hours"]

        pay_period_info.overtime_hours = df.iloc[x]["Overtime Hours"]
        pay_period_info.overtime_hours = df.iloc[x]["Overtime Hours"]

        pay_period_info.income_tax_current_pay_period = df.iloc[x]["Income Tax Current Pay Period"]

        pay_period_info.CPP_current_pay_period = df.iloc[x]["CPP Current Pay Period"]

        pay_period_info.El_current_pay_period = df.iloc[x]["EI Current Pay Period"]

        pay_period_info.benefits_current_pay_period = df.iloc[x]["Benefits Current Pay Period"]

        pay_period_info.pay_period_number = df.iloc[x]["Pay Period #"]

        print(type(pay_period_info.vacation_pay))
        print(type(df.iloc[x]["Holiday Hours"]))

        pay_period_info_list.append(pay_period_info)

    os.remove(uploaded_file_path)
    return pay_period_info_list


