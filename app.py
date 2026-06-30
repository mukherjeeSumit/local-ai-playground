import requests

history = []

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    history.append(f"User: {prompt}")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": "\n".join(history),
            "stream": False
        }
    )

    result = response.json()

    answer = result["response"]

    print("\nAI:", answer)

    history.append(f"Assistant: {answer}")

