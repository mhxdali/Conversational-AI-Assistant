import os
from google import genai
from google.genai import types

api_key = ("YOUR_API_KEY_HERE")  

client = genai.Client(api_key=api_key)


conversation = []

print("Type 'quit' to exit.\n")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break

    conversation.append(
        types.Content(role="user", parts=[types.Part(text=question)])
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conversation,  
        config=types.GenerateContentConfig(temperature=1),
    )

    if response.text:
        print(f"Assistant: {response.text}\n")
    
        conversation.append(
            types.Content(role="model", parts=[types.Part(text=response.text)])
        )
    else:
        print("[No text returned]")
        print(response)
