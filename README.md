# LangChain course

Hands-on LangChain lessons. Lesson 1 calls a chat model and prints the reply.

## Lesson 1: Call a chat model

A chat model takes a list of messages. Each message has a role and text:

- `system` sets how the model should behave
- `human` is the question or task you send
- the model returns an `ai` message

`main.py` builds a system message and a human message, sends them with `invoke`, and prints the reply. OpenAI is the default. A local Ollama model is optional.

## Install

Install [uv](https://docs.astral.sh/uv/), then from this directory:

```bash
uv sync
```

## Configure

Environment variables live in a `.env` file, which git ignores. Copy the placeholder file and edit it:

```bash
cp .env.example .env
```

Set your own key. `your-openai-api-key` is only a placeholder:

```bash
OPENAI_API_KEY=your-openai-api-key
```

Create a key at <https://platform.openai.com/api-keys>.

Optional settings, with the defaults this lesson uses:

```bash
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-4o-mini
```

Exporting the same variables in your shell works too. `main.py` calls `load_dotenv()`, so a `.env` file in the project root is picked up automatically.

### Optional: Ollama

Use a local model with the `langchain-ollama` dependency already in this project. Start Ollama, pull a model, and set:

```bash
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434
```

```bash
ollama pull llama3.2
```

## Run

```bash
uv run python main.py
```

The script prints the provider, the model name, the messages it sent, and the reply. On the OpenAI path, a missing `OPENAI_API_KEY` stops the script with setup instructions before it makes a request.
