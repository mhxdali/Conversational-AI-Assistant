import os
from google import genai
from google.genai import types

api_key = ("API_KEY_HERE")
if not api_key:
    raise SystemExit("GEMINI_API_KEY is not set. Run: export GEMINI_API_KEY="API_KEY_HERE")

client = genai.Client(api_key=api_key)

question = input("Ask something: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=question,
    config=types.GenerateContentConfig(
        temperature=1 # try changing this to 1 later
    ),
)

if response.text:
    print("\n--- Reply ---")
    print(response.text)
else:
    print("\n[No text returned]")
    print(response)
