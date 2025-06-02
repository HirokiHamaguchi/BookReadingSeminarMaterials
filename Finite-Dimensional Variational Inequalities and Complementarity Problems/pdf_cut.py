import os

from PyPDF2 import PdfReader, PdfWriter


def extract_pdf_pages(input_file, output_file, start_page, end_page):
    # PDFを読み込む
    reader = PdfReader(input_file)
    writer = PdfWriter()

    # 指定されたページ範囲のページを追加する
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    # 新しいPDFを保存する
    with open(output_file, "wb") as f:
        writer.write(f)


os.chdir(os.path.dirname(os.path.abspath(__file__)))

input_pdf = "secret\\978-0-387-21814-4_1.pdf"
output_pdf = "secret\\cut_1.pdf"
start = 113  # 切り出し開始ページ（1始まり）
end = 124  # 切り出し終了ページ（1始まり）
extract_pdf_pages(input_pdf, output_pdf, start, end)

input_pdf = "secret\\978-0-387-21814-4_2.pdf"
output_pdf = "secret\\cut_2.pdf"
start = 1  # 切り出し開始ページ（1始まり）
end = 30  # 切り出し終了ページ（1始まり）
extract_pdf_pages(input_pdf, output_pdf, start, end)
