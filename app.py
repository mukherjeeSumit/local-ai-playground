import requests

prompt = input("You: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json ={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()
print("\nAI: ", result["response"])