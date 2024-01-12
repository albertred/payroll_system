from django.core.mail import EmailMessage


def send_email(email_info, pdf_filename):
    print("Start to send email: " + pdf_filename)

    # ...
    # TODO
    # ...

    data_file = open('duck/email/email_template.txt', 'r')
    data = data_file.read()
    print(data)

    # replace string '_employee_name_' with email_info.name
    data = data.replace("_employee_name_", email_info.name)
    data = data.replace("_pay_period_start_", email_info.pay_period_start)
    data = data.replace("_pay_period_end_", email_info.pay_period_end)



    email = EmailMessage(
        'Payroll',
        data,
        'taolu2000@gmail.com',
        [email_info.email_address]
    )

    email.attach_file(pdf_filename)
    email.send()

    print("Email has sent successfully! " + email_info.name)