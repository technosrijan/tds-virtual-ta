# Large Language Models

This module covers the practical usage of large language models (LLMs).

**LLMs incur a cost.** For the May 2025 batch, use aipipe.org as a proxy.
Emails with `@ds.study.iitm.ac.in` get a **$1 per calendar month** allowance. (Don't exceed that.)

Read the AI Pipe documentation to learn how to use it. But in short:

1. Replace `OPENAI_BASE_URL`, i.e. `https://api.openai.com/v1` with `https://aipipe.org/openrouter/v1...` or `https://aipipe.org/openai/v1...`
2. Replace `OPENAI_API_KEY` with the `AIPIPE_TOKEN`
3. Replace model names, e.g. `gpt-4.1-nano`, with `openai/gpt-4.1-nano`

For example, let's use Gemini 2.0 Flash Lite via OpenRouter for chat completions and Text Embedding 3 Small via OpenAI for embeddings:

```bash
curl https://aipipe.org/openrouter/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIPIPE_TOKEN" \
  -d '{
    "model": "google/gemini-2.0-flash-lite-001",
    "messages": [{ "role": "user", "content": "What is 2 + 2?"} }]
  }'

curl https://aipipe.org/openai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AIPIPE_TOKEN" \
  -d '{ "model": "text-embedding-3-small", "input": "What is 2 + 2?" }'
```

Or using `llm`:

```bash
llm keys set openai --value $AIPIPE_TOKEN

export OPENAI_BASE_URL=https://aipipe.org/openrouter/v1
llm 'What is 2 + 2?' -m openrouter/google/gemini-2.0-flash-lite-001

export OPENAI_BASE_URL=https://aipipe.org/openai/v1
llm embed -c 'What is 2 + 2' -m 3-small
```

**For a 50% discount** (but slower speed), use Flex processing by adding `service_tier: "flex"` to your JSON request.

## AI Proxy - Jan 2025

For the Jan 2025 batch, we had created API keys for everyone with an `iitm.ac.in` email to use `gpt-4o-mini` and `text-embedding-3-small`. Your usage is limited to **$1 per calendar month** for this course. Don't exceed that.

**Use AI Proxy** instead of OpenAI. Specifically:

1. Replace your API to `https://api.openai.com/...` with `https://aiproxy.sanand.workers.dev/openai/...`
2. Replace the `OPENAI_API_KEY` with the `AIPROXY_TOKEN` that someone will give you.