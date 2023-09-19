# Resume_Extractor

With the use of natural language processing (NLP) methods, this project intends to develop an automatic PDF extractor and job matching system for resumes (CVs). Data collection is the first step, which entails obtaining job descriptions from the Hugging Face dataset and resumes in PDF format. The fundamental procedure entails PDF parsing to extract text, preprocessing to tidy up and organize the data, and named entity recognition (NER) to extract pertinent information from resumes, such as names, contact information, talents, education, and job experience. The captured text is transformed into numerical vectors using text vectorization methods like TF-IDF. The similarity ratings between resumes and job descriptions are determined by a matching algorithm. These ratings are used to rate resumes.

  The system has a threshold for evaluating if a CV corresponds to a job description, and it produces a ranked list of the best applicants for each position. Measurement measures for evaluation, such as recall and accuracy, assess system performance. Because of the project's adaptability, many NLP models, text vectorization techniques, and matching algorithms may be tested and improved. Transparency and repeatability are guaranteed through documentation. In the end, this project automates the matching of candidates with job criteria, streamlining the hiring process.













## Task 1

This project's goal is to use the Kaggle Resume Dataset to selectively extract key information from a group of CVs submitted in PDF format. This dataset is a handy tool for various data analysis and NLP activities because it contains a wide collection of resumes. To effectively extract crucial information from these resumes, the project requires creating a PDF extractor in Python and using tools like PyPDF2 or PDFMiner.
The primary information that has to be extracted concerns the job function or category, the individuals' talents, and their educational history, which includes information like degrees obtained and schools attended. This research accelerates the process of parsing huge quantities of CVs by automating the extraction of these crucial bits of information, producing a structured and accessible dataset that may be the basis for many applications. The identification of individuals with the necessary credentials and abilities for particular tasks may be made easier with the use of this extracted data, which can be extremely beneficial for human resources, talent acquisition, and job matching procedures. In general, this project fills the gap between structured data and unstructured CV data, improving the efficacy and efficiency of analysing and utilising resume material for various reasons.









## Task 2

This project's goal is to access and comprehend the job descriptions that are part of the Hugging Face dataset. The dataset, which is made up of a number of job descriptions, is useful for several NLP and data analysis applications. The main goal is to extract a subset of 10-15 job descriptions from the dataset using the Hugging Face datasets module, a potent tool for data management and retrieval.
This project makes a variety of job descriptions easily accessible to scholars, data scientists, and NLP practitioners so they can deal with actual employment-related text data. It does this by utilising the Hugging Face datasets collection. A deeper knowledge of the labour market and employment patterns may be achieved by using the extracted job descriptions as useful input for a variety of applications, such as text analysis, information retrieval, and machine learning model training. This initiative not only gives access to rich textual data, but it also has the potential to lead to insightful research and discoveries in the field of text analysis for job descriptions.


## Task 3

Powerful natural language processing (NLP) techniques are being used in this project to automate the process of matching retrieved CV (resume) data with job descriptions. In order to speed up the job-matching process, it includes a number of crucial processes. Job descriptions are first taken from a dataset, maybe from Hugging Face's datasets library, which offers a variety of job posts. In parallel, CV information is taken from PDF files and converted into structured text data that may be used for analysis.
The job matching process may be automated and optimised with the help of this initiative, which will help companies, recruiters, and job seekers all at once. In order to give data-driven insights for effective and accurate CV-to-job description matching, it makes use of the capabilities of cutting-edge NLP models and pretrained embeddings. This eventually improves the recruiting and job-seeking experience.


