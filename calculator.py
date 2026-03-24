"""
LLM Cost Calculator — Compare API pricing across providers.

Usage:
    python calculator.py --tokens-in 500 --tokens-out 300 --requests 1000
    python calculator.py --prompt "Analyze this customer feedback" --requests 5000
"""

import argparse

# Prices per 1M tokens (March 2026)
MODELS = {
    "GPT-4 Turbo": {"input": 10.0, "output": 30.0, "provider": "OpenAI"},
    "GPT-4o": {"input": 2.5, "output": 10.0, "provider": "OpenAI"},
    "GPT-4o Mini": {"input": 0.15, "output": 0.60, "provider": "OpenAI"},
    "Claude 3.5 Sonnet": {"input": 3.0, "output": 15.0, "provider": "Anthropic"},
    "Claude 3 Haiku": {"input": 0.25, "output": 1.25, "provider": "Anthropic"},
    "Gemini 1.5 Pro": {"input": 1.25, "output": 5.0, "provider": "Google"},
    "Gemini 1.5 Flash": {"input": 0.075, "output": 0.30, "provider": "Google"},
    "Llama 3.1 405B": {"input": 3.5, "output": 3.5, "provider": "Together AI"},
    "Llama 3.1 70B": {"input": 0.88, "output": 0.88, "provider": "Together AI"},
    "Mistral Large": {"input": 2.0, "output": 6.0, "provider": "Mistral"},
    "DeepSeek V3": {"input": 0.27, "output": 1.10, "provider": "DeepSeek"},
    "Fine-tuned (self-hosted)": {"input": 0.0, "output": 0.0, "provider": "Your GPU"},
}


def calculate_monthly_cost(model_prices, input_tokens, output_tokens, requests_per_day):
    input_cost = (input_tokens / 1_000_000) * model_prices["input"]
    output_cost = (output_tokens / 1_000_000) * model_prices["output"]
    daily_cost = (input_cost + output_cost) * requests_per_day
    monthly_cost = daily_cost * 30
    return monthly_cost


def estimate_tokens(text: str) -> int:
    return len(text.split()) * 1.3  # rough estimate


def main():
    parser = argparse.ArgumentParser(description="Compare LLM API costs")
    parser.add_argument("--tokens-in", type=int, default=500, help="Avg input tokens per request")
    parser.add_argument("--tokens-out", type=int, default=300, help="Avg output tokens per request")
    parser.add_argument("--requests", type=int, default=1000, help="Requests per day")
    parser.add_argument("--prompt", type=str, help="Sample prompt (auto-estimates tokens)")
    parser.add_argument("--budget", type=float, help="Monthly budget in USD")
    args = parser.parse_args()

    if args.prompt:
        args.tokens_in = int(estimate_tokens(args.prompt))
        print(f"Estimated input tokens: ~{args.tokens_in}")

    print(f"\n{'='*70}")
    print(f"  LLM COST COMPARISON")
    print(f"  Input: {args.tokens_in} tokens | Output: {args.tokens_out} tokens | {args.requests} req/day")
    print(f"{'='*70}\n")
    print(f"{'Model':25s} {'Provider':15s} {'Monthly':>10s} {'Annual':>12s}")
    print(f"{'-'*25} {'-'*15} {'-'*10} {'-'*12}")

    results = []
    for name, prices in MODELS.items():
        monthly = calculate_monthly_cost(prices, args.tokens_in, args.tokens_out, args.requests)
        annual = monthly * 12
        results.append((name, prices["provider"], monthly, annual))

    results.sort(key=lambda x: x[2])

    for name, provider, monthly, annual in results:
        flag = ""
        if args.budget and monthly > args.budget:
            flag = " ⚠️ OVER BUDGET"
        if monthly == 0:
            print(f"{name:25s} {provider:15s} {'$0':>10s} {'$0':>12s}  ← FREE")
        else:
            print(f"{name:25s} {provider:15s} ${monthly:>8.2f} ${annual:>10.2f}{flag}")

    cheapest = results[1]  # skip $0 fine-tuned
    expensive = results[-1]
    savings = expensive[2] - cheapest[2]
    print(f"\n💡 Switching from {expensive[0]} to {cheapest[0]} saves ${savings:.2f}/month (${savings*12:.2f}/year)")
    print(f"💡 Fine-tuning your own model: $0/month — github.com/spinov001-art/ml-fine-tuning-free")


if __name__ == "__main__":
    main()
