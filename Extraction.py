# importing required modules

from PyPDF2 import PdfReader

import sys

import pdfquery

 

# FilePath = ""

# File = ""

 

 

def InvoiceInfo(File):

 

    PDFFile = File

    reader = PdfReader(File)

    pdf = pdfquery.PDFQuery(PDFFile)

    pdf.load(0)

 

    #Invoice Account Number

    label = pdf.pq('LTTextLineHorizontal:contains("Account Number:")')

       

    try:

        topRight = float(label.attr('y1'))

        btmRight_corner = float(label.attr('y0'))

    except TypeError:

        label = pdf.pq('LTTextLineHorizontal:contains("AccountNumber:")')

        btmRight_corner = float(label.attr('y0'))

        topRight = float(label.attr('y1'))

 

    newBtmLeft_Corner = btmRight_corner-190

    newBtmRight_Corner = btmRight_corner+5

    newTopRight_Corner = topRight-80

    newTopLeft_Corner = topRight

    AccountNumber = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (newBtmLeft_Corner, newBtmRight_Corner, newTopRight_Corner, newTopLeft_Corner)).text()

 

    AccountNumber = AccountNumber.replace('Account Number: ', '')

    AccountNumber = AccountNumber.replace('AccountNumber: ', '')

 

 

    return AccountNumber

   

 

File = sys.argv[1]

InvoiceOutput = InvoiceInfo(File)

print(InvoiceOutput)