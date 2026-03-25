import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

QUERIES = [
    "My discount code is not working at checkout.",  # Adapted from wifi driver
    "How do I track the shipping status of my recent order?",  # Adapted from apache logs
    "I forgot my password, how do I reset it?",  # Adapted from account login
    "My item arrived damaged, how do I return it?",  # Adapted from sound update
    "My payment was declined, what should I do?",  # Adapted from printer recognized
    "Why is my delivery taking so long?",  # Adapted from slow internet
    "How do I apply a gift card to my order?",  # Adapted from install chrome
    "The website keeps crashing when I try to pay.",  # Adapted from system freezing
    "Can I change my shipping address after placing an order?",  # Adapted from resize partitions
    "I received the wrong item in my package.",  # Adapted from permission denied
    "How do I cancel my order?",  # Adapted from uninstall software
    "Why was I charged twice for my purchase?",  # Adapted from battery draining
    "I can't find my order in my history.",  # Adapted from bluetooth found
    "The product images are not loading on the page.",  # Adapted from screen flickering
    "When will the out-of-stock items be back?",  # Adapted from update kernel
    "I can't click the 'Place Order' button.",  # Adapted from terminal opening
    "Part of my order is missing from the box.",  # Adapted from missing dependencies
    "Is my credit card information secure on your site?",  # Adapted from setup firewall
    "I want to change the size of the shirt I ordered.",  # Adapted from USB drive
    "The promo code I used didn't apply the discount."  # Adapted from touchpad gestures
]

def load_template(filename):
    with open(os.path.join("prompts", filename), "r") as f:
        return f.read()

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=60)
        response.raise_for_status()
        res_text = json.loads(response.text).get("response", "").strip()
        print("Done.")
        return res_text
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def main():
    zero_shot_template = load_template("zero-shot.txt")
    one_shot_template = load_template("one-shot.txt")

    if not os.path.exists("eval"):
        os.makedirs("eval")

    results_path = os.path.join("eval", "results.md")
    
    with open(results_path, "w", encoding="utf-8") as f:
        f.write("# Chatbot Evaluation Results\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|--------------------|\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Processing Query {i}/20...")
            
            # Zero-Shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            zero_shot_resp = query_ollama(zero_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | Zero-Shot | {zero_shot_resp} | | | |\n")

            # One-Shot
            one_shot_prompt = one_shot_template.format(query=query)
            one_shot_resp = query_ollama(one_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | One-Shot | {one_shot_resp} | | | |\n")

    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    main()
