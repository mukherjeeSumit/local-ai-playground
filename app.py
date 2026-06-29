import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json ={
        "model": "llama3.2:1b",
        "prompt": "In oe sentence, explain what an api is"
        , "stream": False
    }
)

print(response.json()["response"])