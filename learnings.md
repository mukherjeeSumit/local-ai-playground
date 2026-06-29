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

# Progress Tracker

## Project

**Local AI Playground**

### Features Completed

- ✅ Connect Python to Ollama
- ✅ Understand JSON API responses
- ✅ Build an interactive command-line chatbot

### Upcoming Features

- ⏳ Conversation memory
- ⏳ Streaming responses
- ⏳ Prompt templates
- ⏳ Error handling
- ⏳ Better project structure
- ⏳ Documentation

---

# Biggest Lesson So Far

I'm realizing that AI Engineering isn't just about using an LLM.

It's about understanding how software communicates with an LLM, how information flows through the system, and how applications use the structured data returned by the model.