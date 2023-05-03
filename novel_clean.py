import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Sean 是一個非常會講情話的機器人:\n\n You:你好 \n\n Sean:你好美女 You: 你在幹嘛",
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0.0
)
#response 翻成中文
print(response.choices[0].text.strip().replace("\n", ""))
