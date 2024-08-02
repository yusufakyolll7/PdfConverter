from pdf2docx import Converter
pdf_path="samplepdf.pdf"
docx_path="samplepdf.docx"
cv=Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()