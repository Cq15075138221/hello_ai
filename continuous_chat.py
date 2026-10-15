import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url=os.environ.get('DEEPSEEK_BASE_URL', "https://api.deepseek.com")
)

# 保存全部历史：每轮请求都会把之前的 user / assistant 消息一起发给 AI
messages = []

print("连续对话已开始。输入 exit 或 quit 结束。\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages
    )

    assistant_message = response.choices[0].message
    messages.append(assistant_message)
    print(f"AI: {assistant_message.content}\n")
