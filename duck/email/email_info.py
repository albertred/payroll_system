class EmailInfo:
    name = ''
    email_address = ''

    def __str__(self):
        return self.name


def convert_to_email_info(pay_period_info, employee_info):
    email_info = EmailInfo()
    email_info.name = employee_info.employee_name
    email_info.email_address = employee_info.employee_email
    email_info.pay_period_start = str(pay_period_info.pay_period_start.strftime("%Y-%m-%d"))
    email_info.pay_period_end = str(pay_period_info.pay_period_end.strftime("%Y-%m-%d"))


    return email_info
