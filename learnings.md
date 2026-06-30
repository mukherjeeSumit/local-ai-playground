# Local AI Playground – Learning Notes

## Talking to a Local LLM

### What I Built

Built my first Python application that communicates with a local LLM using Ollama.

### Key Concepts

- Ollama acts as a local server that hosts the LLM.
- My Python application communicates with Ollama over HTTP.
- Ollama forwards my request to the model and returns the response.

### Architecture

```text
Python
   │
HTTP Request
   │
   ▼
Ollama
   │
   ▼
Llama 3.2
   │
HTTP Response
   │
   ▼
Python
```

### Biggest Takeaway

My application never communicates directly with the LLM. It always talks to Ollama through an HTTP API.

---

## Understanding JSON Responses

### What I Built

Instead of printing only the AI's answer, I inspected the complete JSON response returned by Ollama.

### Key Concepts

- AI models return structured JSON, not just plain text.
- `response.json()` converts the JSON into a Python dictionary.
- My application decides which fields it wants to use.

### Important Fields

| Field | Purpose |
|--------|----------|
| `response` | The generated answer |
| `model` | Model used to generate the response |
| `created_at` | Timestamp of the response |
| `done` | Indicates whether generation has completed |

### Biggest Takeaway

The response isn't just for the user. It's also for the application.

The user only sees the answer.

The application uses the remaining fields for logging, monitoring, debugging, analytics, and decision-making.

---

## Building an Interactive Chat

### What I Built

Converted my script into a simple interactive chatbot by allowing the user to enter any prompt.

### Key Concepts

- Used Python's `input()` to collect user input.
- Replaced a hardcoded prompt with a dynamic prompt.
- The application stays the same while the user's input changes.

### Architecture

```text
User
   │
Types a prompt
   │
   ▼
Python
   │
HTTP Request
   │
   ▼
Ollama
   │
   ▼
Llama 3.2
   │
HTTP Response
   │
   ▼
Python
   │
Displays response
   │
   ▼
User
```

### Biggest Takeaway

The application doesn't need to change every time a user asks a different question.

The same code can answer unlimited questions because the prompt comes from the user instead of being hardcoded.

---

## Conversation Memory

### What I Built

Added conversation history so the application sends previous messages along with the current prompt.

### Key Concepts

- LLMs do **not** remember previous conversations by themselves.
- Conversation memory is managed by the application, not the model.
- Stored chat history in a Python list.
- Used `"\n".join(history)` to combine the conversation into a single prompt.

### Architecture

```text
User
   │
Current Message
   │
   ▼
Conversation History
   │
   ▼
Python
   │
HTTP Request
   │
   ▼
Ollama
   │
   ▼
Llama 3.2
   │
HTTP Response
   │
   ▼
Python
```

### What I Observed

The model remembered my name because I sent the previous conversation again.

However, after a few messages it started repeating earlier responses instead of answering naturally.

Example:

```
You: My name is Sumit.

AI: Hello Sumit!

You: Explain Airflow.

AI: Airflow is...

You: What is my name?

AI: Hello Sumit! Airflow is...
```

### Why This Happened

I was using Ollama's **generate endpoint**, which treats the entire conversation as one large block of text.

The model simply continues that text instead of understanding separate user and assistant messages.

Modern AI chat applications solve this by using a **Chat API**, where every message has a role such as:

- user
- assistant
- system

This makes conversations much more reliable.

### Biggest Takeaway

The model doesn't have memory.

The application creates the illusion of memory by sending previous messages with every request.

I also learned that **how** we send conversation history matters. Sending one long string works, but using a structured Chat API is the production approach.

---

# Progress Tracker

## Project

**Local AI Playground**

### Features Completed

- ✅ Connect Python to Ollama
- ✅ Understand JSON API responses
- ✅ Interactive command-line chatbot
- ✅ Basic conversation memory

### Upcoming Features

- ⏳ Chat API
- ⏳ Streaming responses
- ⏳ Prompt templates
- ⏳ Error handling
- ⏳ Better project structure
- ⏳ Documentation

---

# Biggest Lessons So Far

1. Applications communicate with LLMs through APIs.
2. AI APIs return structured JSON, not plain text.
3. User input makes applications dynamic.
4. LLMs don't remember conversations—applications do.
5. There are different ways to build chat applications, and using a structured Chat API is more reliable than sending one large text prompt.