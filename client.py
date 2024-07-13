from openai import OpenAI
 

client = OpenAI(
  api_key="sk-proj-h6EeYCwSXwFZNg6nEwoPT3BlbkFJvfkSJoDLa7N4iPbpzuky",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)