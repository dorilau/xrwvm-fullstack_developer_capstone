# Uncomment the imports below before you add the function code
import requests
from urllib.parse import urljoin
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")


def analyze_review_sentiments(text):
    base = sentiment_analyzer_url.rstrip("/") + "/"
    url = urljoin(base, "analyze")
    try:
        resp = requests.post(url, json={"review": text or ""}, timeout=8)
        resp.raise_for_status()
        data = resp.json() if resp.content else {}
        if isinstance(data, dict):
            if "sentiment" in data:
                return data
            if "label" in data:
                return {"sentiment": data["label"]}
        return {"sentiment": "unknown"}
    except Exception as err:
        return {"sentiment": "unknown", "error": str(err)}


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")