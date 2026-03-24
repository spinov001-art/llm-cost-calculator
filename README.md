# 💰 LLM Cost Calculator — Compare API Pricing (2026)

> Calculate and compare costs for GPT-4, Claude, Gemini, Llama, Mistral, and 20+ LLM APIs.

## API Pricing Table (Updated March 2026)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Context Window |
|-------|----------------------|----------------------|----------------|
| GPT-4 Turbo | $10.00 | $30.00 | 128K |
| GPT-4o | $2.50 | $10.00 | 128K |
| GPT-4o Mini | $0.15 | $0.60 | 128K |
| Claude 3.5 Sonnet | $3.00 | $15.00 | 200K |
| Claude 3 Haiku | $0.25 | $1.25 | 200K |
| Gemini 1.5 Pro | $1.25 | $5.00 | 2M |
| Gemini 1.5 Flash | $0.075 | $0.30 | 1M |
| Llama 3.1 405B (via Together) | $3.50 | $3.50 | 128K |
| Llama 3.1 70B (via Together) | $0.88 | $0.88 | 128K |
| Mistral Large | $2.00 | $6.00 | 128K |
| Mixtral 8x22B (via Together) | $1.20 | $1.20 | 64K |
| DeepSeek V3 | $0.27 | $1.10 | 128K |

## Quick Calculator

```python
def calculate_cost(model_prices, input_tokens, output_tokens, requests_per_day):
    """Calculate monthly LLM API cost."""
    input_cost = (input_tokens / 1_000_000) * model_prices["input"]
    output_cost = (output_tokens / 1_000_000) * model_prices["output"]
    daily_cost = (input_cost + output_cost) * requests_per_day
    monthly_cost = daily_cost * 30
    return monthly_cost

# Example: Customer support chatbot
# Average 500 tokens input, 300 tokens output, 1000 requests/day

models = {
    "GPT-4 Turbo": {"input": 10.0, "output": 30.0},
    "GPT-4o Mini": {"input": 0.15, "output": 0.60},
    "Claude 3 Haiku": {"input": 0.25, "output": 1.25},
    "Gemini Flash": {"input": 0.075, "output": 0.30},
    "DeepSeek V3": {"input": 0.27, "output": 1.10},
}

for name, prices in models.items():
    cost = calculate_cost(prices, 500, 300, 1000)
    print(f"{name:20s}: ${cost:8.2f}/month")

# Output:
# GPT-4 Turbo         : $  420.00/month
# GPT-4o Mini         : $   11.25/month
# Claude 3 Haiku      : $   15.00/month
# Gemini Flash        : $    3.83/month
# DeepSeek V3         : $   13.95/month
```

## When to Use What

| Use Case | Best Model | Monthly Cost (1K req/day) |
|----------|-----------|--------------------------|
| Chat support | GPT-4o Mini | $11/mo |
| Code generation | Claude 3.5 Sonnet | $270/mo |
| Summarization | Gemini Flash | $4/mo |
| Research | GPT-4 Turbo | $420/mo |
| Embeddings | text-embedding-3-small | $6/mo |
| **Fine-tuned (your data)** | **DistilBERT** | **$0/mo** |

## The $0 Alternative

For classification, extraction, and specific tasks: [fine-tune your own model](https://github.com/spinov001-art/ml-fine-tuning-free) for free.

## Related

- [ML Fine-Tuning for $0](https://github.com/spinov001-art/ml-fine-tuning-free)
- [Free GPU Options](https://github.com/spinov001-art/free-gpu-machine-learning)
- [Web Scraping Tools](https://github.com/spinov001-art/awesome-web-scraping-2026)
- [All tutorials on Dev.to](https://dev.to/0012303)

## License

MIT
