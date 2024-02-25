'''
from openai import OpenAI

client = OpenAI(
    api_key = "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"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "List 10 animals"}],
    stream=False
)

print(response.choices[0].message.content)


from openai import OpenAI

client = OpenAI(
    api_key = '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'
)

response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role':'system', 'content':'You are a helpful assistant.'},
        {'role':'user', 'content':'Who won the world series in 2020?'},
        {'role':'assistant', 'content':'The Los Angeles Dodgers won the World Series in 2020'},
        {'role':'user', 'content':'Where was it played?'}
    ]
)

print(response)
print(response.choices[0].message.content)





    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    return response.choices[0].message.content

# Examples
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I've been having headaches recently."},
    {"role": "assistant", "content": "How long have you been experiencing these headaches?"},
    {"role": "user", "content": "For about two weeks now."}
]

next_reply = simulate_medical_conversation(conversation_history)
print("Assistant's next reply:", next_reply)





# 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
from openai import OpenAI

client = OpenAI(
    api_key='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'
)

def create_chat_completion(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system", "content":"You are a helpful assistant."},
            *prompt
        ]
    )
    return response.choices[0].message.content

# Initialize
conversation_history = []

# Examples
conversation_history = [
    {"role": "system", "content": "You are a knowledgeable medical doctor."},
    {"role": "user", "content": "I've been having headaches recently."},
    {"role": "assistant", "content": "How long have you been experiencing these headaches?"},
    {"role": "user", "content": "For about two weeks now."}
]

# Simulate dialogue
def simulate_conversation(user_input):
    global conversation_history
    session_id = "headache01"

    conversation_history.append({"role":"user", "content":"user_input"})

    reply = create_chat_completion(conversation_history)

    conversation_history.append({"role": "assistant", "content":reply})

    return reply

# print(simulate_conversation("I have a headache."))
# print(simulate_conversation("It started two days ago."))
print(simulate_conversation("What is possible causing my symptoms?"))
print("好的")
print(simulate_conversation("What should I do to release my headache?"))



from openai import OpenAI

client = OpenAI(
    api_key = "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"
)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)

'''
from openai import OpenAI
import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/Users/a200/Desktop/111.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

#print(response.json())
print(response.json()['choices'][0]['message']['content'])