"""Lesson 1: call a chat model.

A chat model talks in messages. Each message has a role and text:

- system: instructions for how the model should behave
- human: the question or task you send
- ai: the model's reply (you usually only build the first two)

This script loads settings from the environment, builds one of those message
lists, sends it with ``invoke``, and prints the reply. OpenAI is the default.
Set ``LLM_PROVIDER=ollama`` to call a local model instead.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
DEFAULT_OLLAMA_MODEL = "llama3.2"
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"


def lesson_messages() -> list[SystemMessage | HumanMessage]:
    """The conversation this lesson sends. Edit the human message and rerun."""
    return [
        SystemMessage(
            content=(
                "You teach LangChain to a developer who just made their first "
                "chat-model call. Be concrete. Stay under 120 words."
            )
        ),
        HumanMessage(
            content=(
                "This request was sent as a system message plus a human message "
                "through LangChain's invoke(). What is each role for, and what "
                "should I look at in your reply to confirm the call worked?"
            )
        ),
    ]


def build_chat_model():
    """Return a chat model selected by LLM_PROVIDER (openai or ollama)."""
    provider = os.getenv("LLM_PROVIDER", "openai").strip().lower()

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise SystemExit(
                "OPENAI_API_KEY is not set.\n"
                "Copy .env.example to .env and set OPENAI_API_KEY there, "
                "or export it in your shell.\n"
                "For a local model instead, run:\n"
                "  LLM_PROVIDER=ollama uv run python main.py"
            )
        model_name = os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL).strip()
        return ChatOpenAI(model=model_name, temperature=0), provider, model_name

    if provider == "ollama":
        model_name = os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL).strip()
        base_url = os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL).strip()
        chat = ChatOllama(model=model_name, base_url=base_url, temperature=0)
        return chat, provider, model_name

    raise SystemExit(f"Unknown LLM_PROVIDER={provider!r}. Use 'openai' or 'ollama'.")


def main() -> None:
    load_dotenv()
    chat, provider, model_name = build_chat_model()
    messages = lesson_messages()

    print(f"Calling {provider} model {model_name}")
    print("Messages sent:")
    for message in messages:
        print(f"  [{message.type}] {message.content}")
    print()

    reply = chat.invoke(messages)
    print(f"Reply type: {type(reply).__name__}")
    print(reply.content)


if __name__ == "__main__":
    main()
