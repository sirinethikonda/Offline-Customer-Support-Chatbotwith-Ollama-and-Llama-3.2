# Offline Customer Support Chatbot

A private, secure, and cost-effective customer support chatbot built using **Ollama** and the **Llama 3.2 3B** model. This project focuses on evaluating different prompting techniques (Zero-Shot vs. One-Shot) for e-commerce support scenarios.

---

## Key Features
- **Data Privacy**: All processing happens locally; no customer data ever leaves your machine.
- **Cost Effective**: utilizes open-source models with zero API inference costs.
- **Prompt Engineering**: comparisons between Zero-Shot and One-Shot prompting strategies.
- **Evaluation Framework**: includes a structured rubric for assessing model performance.

---

## Tools & Technologies
- **Ollama**: Local LLM runner.
- **Llama 3.2 3B**: Lightweight, high-performance language model.
- **Python 3.x**: Scripting and automation.
- **Requests**: Python library for API interaction.

---

## Prerequisites
- **Ollama** installed (Download from [ollama.com](https://ollama.com/)).
- **Llama 3.2 3B** model pulled.
- **Python 3.8+** installed.

---

## Setup Instructions

### 1. Pull the Model
Open your terminal and run:
```bash
ollama pull llama3.2:3b
```

### 2. Python Environment Setup
Create a virtual environment and install the required dependencies:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install requests datasets
```

---

## Testing the Connection
Before running the full evaluation, verify that Ollama is responding correctly using the provided test script:

```bash
python test.py
```
This script checks if the Ollama API is reachable and if the `llama3.2:3b` model is loaded and ready to respond.

---

## How to Run
To run the automated evaluation script:
```bash
python chatbot.py
```
This will process 20 e-commerce queries and save the responses to `eval/results.md`.

---

## Evaluation Results Summary
Based on our comparison between **Zero-Shot** and **One-Shot** prompting:

| Prompting Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|------------------|---------------|---------------|-----------------|
| **Zero-Shot**    | 4.85          | 5.0           | 4.65            |
| **One-Shot**     | 4.85          | 4.95          | 4.0             |

> [!NOTE]
> Zero-Shot prompting proved surprisingly robust for general e-commerce tasks, while One-Shot sometimes introduced unnecessary caution or disclaimers.

---

## Project Structure
- `chatbot.py`: Main script to interact with the Ollama API.
- `test.py`: Quick connection test script.
- `prompts/`: Directory containing `.txt` files for different prompting strategies.
- `eval/`: Directory where evaluation results are stored.
- `report.md`: Detailed analysis and conclusion of the project.
- `setup.md`: Quick setup reference.
