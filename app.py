from flask import Flask, render_template, request
import requests
import pymongo
app = Flask(__name__)


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
