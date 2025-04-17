import glob
import os
import fitz


def pdf2png(pdf_file):
    doc = fitz.open(pdf_file)
    page = doc.load_page(0)
    pixmap = page.get_pixmap(dpi=300)
    pixmap.save(pdf_file.replace(".pdf", ".png"), "png")


def main():
    os.chdir(
        r"C:\Users\hirok\Documents\University\BookReadingSeminarMaterials\20241002\hobby"
    )
    for pdf_file in glob.glob("*.pdf"):
        pdf2png(pdf_file)
        print(f"Converted {pdf_file} to png")


if __name__ == "__main__":
    main()
