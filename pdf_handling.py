# pdf_handling.py
from reportlab.pdfgen import canvas
from PyPDF4 import PdfFileReader, PdfFileWriter
from reportlab.lib.pagesizes import letter
import io

# Функция для создания текстового наложения
def create_text_overlay(text_items):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    for item in text_items:
        c.setFont(item['font'], item['font_size'])
        c.drawString(item['x'], item['y'], item['text'])
    c.save()
    packet.seek(0)
    return packet

# Функция для добавления текстового слоя на PDF
def add_text_to_pdf(input_pdf_path, text_items):
    text_overlay_pdf_stream = create_text_overlay(text_items)
    text_pdf = PdfFileReader(text_overlay_pdf_stream)

    original_pdf = PdfFileReader(open(input_pdf_path, "rb"))
    writer = PdfFileWriter()

    page = original_pdf.getPage(0)
    page.mergePage(text_pdf.getPage(0))
    writer.addPage(page)
    for num in range(1, original_pdf.getNumPages()):
        writer.addPage(original_pdf.getPage(num))

    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf
