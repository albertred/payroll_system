import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter




def print_decimal(d):
    return "%.2f" % d


def generate_pdf(pay_period_info, employee_info):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    can.setFont("Helvetica", 10)

    can.drawString(341, 530, "CPP")
    can.drawString(341, 514, "EI")
    can.drawString(341, 498, "INCOME TAX")
    can.drawString(341, 482, "BENEFITS")

    can.drawRightString(568, 702, str(pay_period_info.pay_period_number))

    can.drawString(140, 655, employee_info.employee_name)
    can.drawString(140, 640, employee_info.employee_id)

    can.drawString(112, 609, pay_period_info.pay_period_start.strftime("%Y-%m-%d"))
    can.drawString(220, 609, pay_period_info.pay_period_end.strftime("%Y-%m-%d"))
    can.drawString(185, 609, "TO")
    can.drawString(155, 594, pay_period_info.pay_date.strftime("%Y-%m-%d"))

    can.drawRightString(320, 485, print_decimal(pay_period_info.vacation_pay))
    can.drawRightString(239, 470, print_decimal(pay_period_info.holiday_hours))

    can.drawRightString(158, 530, print_decimal(pay_period_info.regular_rate))
    can.drawRightString(239, 530, print_decimal(pay_period_info.regular_hours))
    can.drawRightString(320, 530, print_decimal(pay_period_info.regular_current_total))

    can.drawRightString(158, 514, print_decimal(pay_period_info.OFFOT_time_rate))
    can.drawRightString(239, 514, print_decimal(pay_period_info.OFFOT_time_hours))
    can.drawRightString(320, 514, print_decimal(pay_period_info.OFFOT_time_current_total))

    can.drawRightString(158, 502, print_decimal(pay_period_info.overtime_rate))
    can.drawRightString(239, 502, print_decimal(pay_period_info.overtime_hours))
    can.drawRightString(320, 502, print_decimal(pay_period_info.overtime_current_total))

    can.drawRightString(477, 530, print_decimal(round(pay_period_info.CPP_current_pay_period, 2)))
    can.drawRightString(568, 530, print_decimal(round(pay_period_info.CPP_ytd, 2)))

    can.drawRightString(477, 515, print_decimal(round(pay_period_info.El_current_pay_period, 2)))
    can.drawRightString(568, 515, print_decimal(round(pay_period_info.El_ytd, 2)))

    can.drawRightString(477, 498, print_decimal(round(pay_period_info.income_tax_current_pay_period, 2)))
    can.drawRightString(568, 498, print_decimal(round(pay_period_info.income_tax_ytd, 2)))

    can.drawRightString(475, 483, print_decimal(round(pay_period_info.benefits_current_pay_period, 2)))
    can.drawRightString(568, 483, print_decimal(round(pay_period_info.benefits_ytd, 2)))

    can.drawRightString(409, 375, print_decimal(round(pay_period_info.gross_total, 2)))
    can.drawRightString(477, 375, print_decimal(round(pay_period_info.deductions, 2)))
    can.drawRightString(568, 375, print_decimal(round(pay_period_info.net_pay, 2)))

    can.drawRightString(89, 375, print_decimal(pay_period_info.YTD_payroll))
    can.drawRightString(158, 375, print_decimal(pay_period_info.YTD_vacation))
    can.drawRightString(239, 375, print_decimal(pay_period_info.YTD_deductions))
    can.drawRightString(320, 375, print_decimal(pay_period_info.YTD_net_pay))

    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)
    # read your existing PDF

    existing_pdf = PyPDF2.PdfFileReader(open("./duck/pdf/AAP-blank.pdf", "rb"))
    output = PyPDF2.PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    file_name = employee_info.employee_name + "_" + employee_info.employee_id + "_" + str(pay_period_info.pay_period_number) + ".pdf"
    output_stream = open(file_name, "wb")
    output.write(output_stream)
    output_stream.close()

    existing_pdf.stream.close()

    return file_name
