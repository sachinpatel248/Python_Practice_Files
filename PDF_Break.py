from PyPDF2 import PdfFileWriter, PdfFileReader

source_PDF_File_Path = r'AbsSummarization.pdf'

input_PDF = PdfFileReader(open(source_PDF_File_Path, "rb"))
##print(inputpdf.numPages)

input_page_Obj = input_PDF.getPage(5)
input_page_Text = input_page_Obj.extractText()

text_required = []
text_required.append('Problem Motivation')
text_required.append('Novel Contribution')

output = PdfFileWriter()
    
for i in range(input_PDF.numPages):
    print(i)
    input_page_Obj = input_PDF.getPage(i)
    input_page_Text = input_page_Obj.extractText()

    found = False

    for text in text_required:
        text = text.lower()
        text = text.replace(' ','')
 
        if text in input_page_Text.lower():
            new_output = PdfFileWriter()
            new_output.addPage(input_PDF.getPage(i))
            found = True
            file_Name = str(text)+ "_" + str(i) + ".pdf"

            with open(file_Name, "wb") as outputStream:
                new_output.write(outputStream)

    if found == False:
        output.addPage(input_PDF.getPage(i))

with open("document-page.pdf", "wb") as outputStream:
    output.write(outputStream)

