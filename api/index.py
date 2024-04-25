from flask import Flask, request
import requests

app = Flask(__name__)

@app.get("/")
async def home():
    return "Hello, World!"

@app.get("/chat-exporter")
async def chat():
    url = request.query_string.decode("utf-8").replace("url=", "")
    decoded_url = unquote(url)
    content = requests.get(decoded_url).text
    return content
