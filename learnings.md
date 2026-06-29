# Day 1

## What I built

A Python application that communicates with a local LLM through Ollama.

## Biggest takeaway

Python doesn't talk directly to the model.

It sends an HTTP request to Ollama, which forwards the request to the model and returns the response.

## Architecture

Python → HTTP → Ollama → Llama 3.2 → Response