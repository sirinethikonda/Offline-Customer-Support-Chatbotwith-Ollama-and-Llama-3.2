# Setup Instructions

## 1. Install Ollama
Download and install Ollama from [ollama.com](https://ollama.com/).

## 2. Pull the Model
Run the following command in your terminal:
```bash
ollama pull llama3.2:3b
```

## 3. Python Environment
Create a virtual environment and install dependencies:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install requests datasets
```

## 4. Run the Chatbot
```bash
python chatbot.py
```
