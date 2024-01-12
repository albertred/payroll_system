from database.database_accessor import read_pay_period_list_by_employ_id, save, retrieve_employee_info_from_db
from duck.calculator.calculator import calculate
from duck.email.email_info import convert_to_email_info
from duck.email.email_sender import send_email
from duck.excel.pay_period_reader import read_from_excel, validate_excel
from duck.pdf.pay_stub_generator import generate_pdf
# from duck.pdf.pay_stub_info import convert_to_pay_stub
from duck.processor.process_result import ProcessResult


def process(uploaded_file_path):
    validate_result = validate_excel(uploaded_file_path)

    if validate_result:
        pay_period_info_list = read_from_excel(uploaded_file_path)

        for pay_period_info in pay_period_info_list:
            # list of model objects
            list_of_pay_period = list(read_pay_period_list_by_employ_id(pay_period_info.employee_id))

            pay_period_info = calculate(pay_period_info, list_of_pay_period)

            save(pay_period_info)  # for next period

            employee_info = retrieve_employee_info_from_db(pay_period_info.employee_id)
            pdf_filename = generate_pdf(pay_period_info, employee_info)
            print('pdf file name: ' + pdf_filename)

            email_info = convert_to_email_info(pay_period_info, employee_info)
            send_email(email_info, pdf_filename)

        result = ProcessResult()
        return result
    else:
        result = ProcessResult()
        result.result = "Oops, you have got wrong file!"
        return result
