import PyPDF2

a = PyPDF2.PdfFileReader('sample.pdf')

str = " "

for i in range (1,2):
  str += a.getPage(i).extractText()

with open("text1.txt", "w", encoding='utf-8') as f:
  f.write(str)