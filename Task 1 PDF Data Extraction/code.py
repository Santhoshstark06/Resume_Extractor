!pip install PyPDF2
!pip install pdfminer.six
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import PyPDF2
!pip install PdfReader


import PyPDF2


with open(), rb1 as pdf_file:

pdf_reader=PyPDF2.PdfReader(pdf file)
page pdf reader pages[0]
x=page extract_text()



def extract_details(text):

    category_match=re.searcher(r'Category:(+?)\n', text)
    category=category_match.group(1)if category match else None

    skills match re search(r Skills (+7)\n text) 
    skills= skills_match group(1) if skills_match else None
    education_match = re searcher Education (+7)\n. text)
    education= education_match.group (1) if education match else None

    return category. skills, education
print extract_details(x))

