import requests
import pymongo, sys
hf_token = "hf_token"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:
 response = requests.post(
   embedding_url,
   headers={"Authorization": f"Bearer {hf_token}"},
   json={"inputs": text})
 if response.status_code != 200:
   raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
 return response.json()


URI = "mongo_URI"
conn = pymongo.MongoClient(URI)
db = conn['sample_mflix']
coll = db['movies']


for doc in coll.find({"plot":{"$exists": True},"plot_embedding_hf":{"$exists": False}}).limit(200):
       doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
       db['movie_embeded'].insert_one(doc)
       print(doc["_id"])
