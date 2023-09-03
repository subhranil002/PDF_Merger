from PyPDF2 import PdfWriter
import os


def pdfMarger(pdfFiles):
    print("Initializing...")
    merger = PdfWriter()

    print("Marging...")
    for pdf in pdfFiles:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()
    print("Successfully Marged!")


pdfFiles = ["example1.pdf", "example2.pdf"]
pdfMarger(pdfFiles)
