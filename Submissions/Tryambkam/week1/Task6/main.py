#before running the python script make sure you have installed the PyPDF2 python library
#using pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

#in file_path assign path of pdf file from which you want extract the text

import PyPDF2
a = PyPDF2.PdfFileReader('Sample1.pdf')
str = " "
for i in range(3,5):
   str += a.getPage(i).extractText()
with open("text.txt", "w", encoding= 'utf-8') as f:
    f.write(str)   