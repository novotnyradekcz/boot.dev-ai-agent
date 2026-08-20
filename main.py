import os

from dotenv import load_dotenv
from openai import OpenAI

_ = load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("`OPENROUTER_API_KEY` not set. Add it to your .env file.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
)

if response.usage is None:
    raise RuntimeError("`response.usage` is None. API request likely failed.")

print(f"User prompt: {user_prompt}")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")
print(f"Response:\n{response.choices[0].message.content}")
