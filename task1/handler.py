import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()  # Loads your key from a .env file
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_customer_message(message):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful telecom support assistant."},
                {"role": "user", "content": message}
            ],
            timeout=5.0  # Required 5s timeout
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error occurred: {e}")
        return "I'm having trouble connecting to my brain. Please hold."

if __name__ == "__main__":
    reply = asyncio.run(handle_customer_message("My internet is slow"))
    print(f"AI: {reply}")