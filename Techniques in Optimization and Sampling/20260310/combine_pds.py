import os
from pathlib import Path

import PyPDF2

os.chdir(Path(__file__).parent)

# memo.pdfと、../secret/cut_main.pdfと、..\secret\1-s2.0-S0022000005000966-main.pdfをこの順番で結合して、combined.pdfを作成するコード

# PDFファイルのパスを指定
pdf_files = [
    "memo.pdf",
    "../secret/cut_main.pdf",
    "../secret/1-s2.0-S0022000005000966-main.pdf",
]

# PDFマージャーを作成
merger = PyPDF2.PdfMerger()

# 各PDFファイルを追加
for pdf_file in pdf_files:
    merger.append(pdf_file)

# 結合したPDFを出力
merger.write("combined.pdf")
merger.close()

print("combined.pdf を作成しました")
