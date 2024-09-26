import requests
import pymongo, sys
from dotenv import load_dotenv
import os

hf_token = os.getenv('hf_token')
embedding_url = os.getenv('embedding_url')


def generate_embedding(text: str) -> list[float]:
 response = requests.post(
   embedding_url,
   headers={"Authorization": f"Bearer {hf_token}"},
   json={"inputs": text})
 if response.status_code != 200:
   raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
 return response.json()


URI = os.getenv('URI')
conn = pymongo.MongoClient(URI)
db = conn['sample_mflix']
coll = db['movies']


for doc in coll.find({"plot":{"$exists": True},"plot_embedding_hf":{"$exists": False}}).limit(200):
       doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
       db['movie_embeded'].insert_one(doc)
       print(doc["_id"])
