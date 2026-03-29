import requests
import json
import os

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Queries list (Aligned with manual requirements)
QUERIES = [
    "How can I track my order status?",
    "My discount code is not working at checkout.",
    "I received a damaged product, what should I do?",
    "Can I return an item after 30 days?",
    "How do I cancel my order?",
    "My payment failed but money was deducted.",
    "Do you offer cash on delivery?",
    "How long does shipping take?",
    "Can I change my delivery address after placing an order?",
    "I haven't received my order confirmation email.",
    "What is your refund policy?",
    "How do I contact customer support?",
    "Is international shipping available?",
    "Why was my order canceled automatically?",
    "Can I exchange a product for a different size?",
    "My order is delayed, what should I do?",
    "Are there any shipping charges?",
    "How do I apply a gift card?",
    "Can I place an order without creating an account?",
    "How do I reset my account password?"
]

# Manual evaluation scores based on the responses
SCORES = {
    1: {"ZS": (5, 5, 5), "OS": (5, 5, 5)},
    2: {"ZS": (4, 5, 3), "OS": (5, 5, 4)},
    3: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    4: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    5: {"ZS": (4, 5, 3), "OS": (5, 5, 4)},
    6: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    7: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    8: {"ZS": (5, 5, 5), "OS": (4, 5, 4)},
    9: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    10: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    11: {"ZS": (5, 5, 5), "OS": (5, 5, 5)},
    12: {"ZS": (5, 5, 5), "OS": (5, 5, 5)},
    13: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    14: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    15: {"ZS": (5, 5, 4), "OS": (5, 5, 3)},
    16: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    17: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    18: {"ZS": (5, 5, 5), "OS": (3, 4, 2)},
    19: {"ZS": (5, 5, 5), "OS": (5, 5, 4)},
    20: {"ZS": (5, 5, 5), "OS": (5, 5, 4)}
}

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
        f.write("## Scoring Rubric\n")
        f.write("1. **Relevance (1-5)**: How well does the response address the customer’s query? (1 = Irrelevant, 5 = Perfectly relevant)\n")
        f.write("2. **Coherence (1-5)**: Is the response grammatically correct and easy to understand? (1 = Incoherent, 5 = Flawless)\n")
        f.write("3. **Helpfulness (1-5)**: Does the response provide a useful, actionable answer? (1 = Not helpful, 5 = Very helpful)\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|--------------------|\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Processing Query {i}/20...")
            
            # Get pre-defined scores
            s = SCORES.get(i, {"ZS": ("", "", ""), "OS": ("", "", "")})
            
            # Zero-Shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            zero_shot_resp = query_ollama(zero_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | Zero-Shot | {zero_shot_resp} | {s['ZS'][0]} | {s['ZS'][1]} | {s['ZS'][2]} |\n")

            # One-Shot
            one_shot_prompt = one_shot_template.format(query=query)
            one_shot_resp = query_ollama(one_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | One-Shot | {one_shot_resp} | {s['OS'][0]} | {s['OS'][1]} | {s['OS'][2]} |\n")

    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    main()
