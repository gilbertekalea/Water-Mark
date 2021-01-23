import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merge = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merge.append(pdf)
    merge.write('super.pdf')
pdf_combiner(inputs)