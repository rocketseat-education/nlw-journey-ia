from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagens para mim."},
  ]
)

print(response.choices[0].message.content)