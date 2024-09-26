from flask import Flask, render_template, request
import requests
import pymongo
from dotenv import load_dotenv
import os
app = Flask(__name__)


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


@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == 'POST':
        query = request.form['search_term']
        pipeline = [
            {"$vectorSearch": {
                "queryVector": generate_embedding(query),
                "path": "plot_embedding_hf",
                "numCandidates": 100,
                "limit": 6,
                "index": "PlotSemanticSearch",
                }}
        ]
        
        result = list(coll.aggregate(pipeline))
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True,port=2408)
