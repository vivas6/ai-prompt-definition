import openai
import os

openai.api_key  = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

def callOpenAI(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content