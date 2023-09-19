import PyPDF2
import csv
import os

from os import listdir

from os.path import isfile, join

def extract text from pdf (pdf path):
    text=""
    with open(pdf path, 'rb') as pdf_file:
        pdf reader PyPDF2.PdfReader (pdf file)
        for page num in range(pdf reader.numPages):
            text+= pdf reader.getPage(page_num).extractText()
            return text
def extract details from pdf (pdf_path):
    pdf text extract text from pdf (pdf_path)
            
            
    category match re.search(r Category: 1.7)\n, pdf_text) 
    category category match.group(1) if category match else None
    
    skills match = re.search(r Skills: (+7)\n", pdf_text)
    skills skills match.group(1) if skills match else None

    education match re.search('Education (+7)\n', pdf_text)
    education=education_match.group(1) if education_match else None
       return category, skills, education

pdf_directory 'c://home/SanthoshKumar/Desktop/DataAnalysis/ACCOUNTANT
print (pdf_directory)

csv filename = 'extracted details.csv'
csv file = open(csv filename, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["File", 'Category', 'Skills', 'Education'])

for filename in os.listdir(pdf_directory):
    if filename.endswith(.pdf):
        pdf_path= os.path.join(pdf directory, filename!
        category, skills, education extract_details_from_pdf(pdf_path)
         csv_writer.writerow( [filename, category, skills, education])

csv_file.close()
print("Extracted details saved to (csv_filename}")                      
                             
