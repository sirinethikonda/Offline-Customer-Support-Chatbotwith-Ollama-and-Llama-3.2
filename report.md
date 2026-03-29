# Chatbot Evaluation Report

## 1. Introduction
This report evaluates the performance of a local LLM (**Llama 3.2 3B**) for customer support in an e-commerce context. We compared **Zero-Shot** vs. **One-Shot** prompting techniques across 20 common customer queries.

## 2. Methodology
- **Dataset**: 20 queries adapted from the Ubuntu Dialogue Corpus to fit e-commerce scenarios.
- **Model**: Llama 3.2 3B running locally via Ollama.
- **Scoring Rubric (1-5)**:
  - **Relevance**: How well the response addresses the query.
  - **Coherence**: Grammatical correctness and readability.
  - **Helpfulness**: Usefulness and actionability.

## 3. Results & Analysis

### Quantitative Summary
| Prompting Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|------------------|---------------|---------------|-----------------|
| **Zero-Shot**    | 4.85          | 5.0           | 4.65            |
| **One-Shot**     | 4.85          | 4.95          | 4.0             |

### Qualitative Observations
- **Zero-Shot**: Surprisingly consistent and helpful. The model relied on its general training to provide standard support procedures (e.g., "clear cache", "check order history").
- **One-Shot**: While expected to be better, the single example sometimes led the model to be *too* cautious or deviate into "I'm just an AI" disclaimers when the specific example didn't perfectly match the query (e.g., Query 2 and 12).
- **Inference Speed**: Local execution on CPU was slow (~1 minute per query), confirming the trade-off for data privacy.

## 4. Conclusion & Limitations
Llama 3.2 3B is highly suitable for basic customer support triage. It demonstrates excellent understanding of e-commerce concepts. 

**Limitations**:
- **Latency**: High response time on consumer hardware.
- **Context**: The model lacks real-time access to order databases (hallucinated "Order History" sections).
- **One-Shot Tuning**: A single example is a good start, but multi-shot or fine-tuning would be more robust.

**Next Steps**:
- Integrate with a real database for order tracking.
- Implement few-shot prompting with diverse examples.
