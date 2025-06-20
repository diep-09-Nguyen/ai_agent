import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
env_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=env_key)

user_prompt = sys.argv[1]
verbose = None
if len(sys.argv) > 2:
    verbose = sys.argv[2]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages
)

if response.text:
    print(response.text)
    if verbose:
        print(f"User prompt: {user_prompt}")
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
