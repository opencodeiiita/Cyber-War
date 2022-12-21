from PyPDF2 import PdfFileReader

pdf = PdfFileReader('/home/kali/Downloads/test.pdf')

with open('pdf.txt','w') as t:

    text = ''
    for page in pdf.pages:
        text = text + page.extractText()
    t.write(text)
