from flask import Flask, request
import requests

app = Flask(__name__)

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.get("/chat-exporter")
async def chat():
    url = request.query_string.decode("utf-8").replace("url=", "")
    content = requests.get(url).text
    return content

app.run(host="0.0.0.0", port=5000)
