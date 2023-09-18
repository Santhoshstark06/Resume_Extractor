pip install transformers numpy
import numpy as np
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertModel.from_pretrained(model_name)
def get_embeddings(text, tokenizer, model):
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1).numpy()
def calculate_similarity(job_description_embedding, cv_embeddings):
    similarities = cosine_similarity(job_description_embedding, cv_embeddings)
    return similarities
def rank_cvs(job_description, cv_details, tokenizer, model):
    job_description_embedding = get_embeddings(job_description, tokenizer, model)
    cv_embeddings = get_embeddings(cv_details, tokenizer, model)
    similarities = calculate_similarity(job_description_embedding, cv_embeddings)
    ranking = np.argsort(similarities[0])[::-1]  # Sort in descending order
    top_5_cvs = ranking[:5]
    return top_5_cvs
job_descriptions = [...]  
cv_details = [...]  

for job_description in job_descriptions:
    top_5_cvs = rank_cvs(job_description, cv_details, tokenizer, model)
    print("Job Description:", job_description)
    print("Top 5 Matching CVs:")
    for idx in top_5_cvs:
        print(cv_details[idx])
    print("\n")
