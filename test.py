import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2:3b",
    "prompt": "Give a short customer support greeting.",
    "stream": False
}

try:
    print("Testing connection to Ollama...")
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    data = json.loads(response.text)
    print("Model Response:", data.get("response"))
    print("\nSuccess! Ollama is reachable and the model is responding.")

except requests.exceptions.RequestException as e:
    print(f"Error connecting to Ollama: {e}")
    print("\nMake sure Ollama is running and the model 'llama3.2:3b' is pulled.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
