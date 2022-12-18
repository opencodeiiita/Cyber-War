#before running the python script make sure you have installed the PyPDF2 python library
#using pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

#in file_path assign path of pdf file from which you want extract the text

file_path = '/home/jaydeepxx/Desktop/sample.pdf'
pdf = PdfFileReader(file_path)


#below code writing the extracted text from pdf to "sample.txt" 

with open('sample.txt','w') as f:
    for page_num in range(pdf.numPages):
        print('PAge: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100,'-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)

    f.close()

#this script will create a sample.txt text file in which the extracted text will be present
