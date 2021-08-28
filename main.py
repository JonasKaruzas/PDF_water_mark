import PyPDF2

pdf_w = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
pdf2 = PyPDF2.PdfFileReader(open('dummy.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf2.getNumPages()):
    page = pdf2.getPage(i)
    page.mergePage(pdf_w.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
