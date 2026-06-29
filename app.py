import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json ={
        "model": "llama3.2:1b",
        "prompt": "In one sentence, explain what an api is",
        "stream": False
    }
)

result = response.json()
print(result["response"])