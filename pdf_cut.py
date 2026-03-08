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

input_pdf = r"Techniques in Optimization and Sampling\secret\main.pdf"
output_pdf = r"Techniques in Optimization and Sampling\secret\cut_main.pdf"
start = 160  # 切り出し開始ページ（1始まり）
end = 170  # 切り出し終了ページ（1始まり）
extract_pdf_pages(input_pdf, output_pdf, start, end)
