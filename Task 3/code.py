import torch
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity


job_descriptions = ["Job description 1 text here.", "Job description 2 text here.", ...] 
cvs = ["CV 1 text here.", "CV 2 text here.", ...] 


tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

job_description_embeddings = []
cv_embeddings = []

for job_description in job_descriptions:
    tokens = tokenizer(job_description, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        output = model(**tokens)
    job_description_embeddings.append(output.last_hidden_state.mean(dim=1).numpy())

for cv in cvs:
    tokens = tokenizer(cv, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        output = model(**tokens)
    cv_embeddings.append(output.last_hidden_state.mean(dim=1).numpy())


similarity_scores = cosine_similarity(job_description_embeddings, cv_embeddings)


top_5_cvs_per_job_description = []

for i, job_description in enumerate(job_descriptions):
    cv_scores = list(enumerate(similarity_scores[i]))
    sorted_cvs = sorted(cv_scores, key=lambda x: x[1], reverse=True)[:5]
    top_5_cvs = [(cvs[idx], score) for idx, score in sorted_cvs]
    top_5_cvs_per_job_description.append((job_description, top_5_cvs))
