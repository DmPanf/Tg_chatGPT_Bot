# import the necessary packages
import json
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Load the environment variables from the env.json file
with open('env.json', 'r') as f:
    env = json.load(f)

TELEGRAM_BOT_TOKEN = env['TELEGRAM_BOT_TOKEN']
CHATGPT_API_KEY = env['CHATGPT_API_KEY']
DATA_STORAGE_FILE = env['DATA_STORAGE_FILE']

# Create a new instance of the Telegram Bot:
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Define a function to handle incoming messages

async def handle_message(message: types.Message):
    # Send the user's message to the ChatGPT API
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={'Authorization': f'Bearer {CHATGPT_API_KEY}'},
        json={
            'prompt': message.text,
            'max_tokens': 50,
            'temperature': 0.7
        }
    )

    # Save the request and response to the data storage file
    with open(DATA_STORAGE_FILE, 'a') as f:
        f.write(f'Request: {message.text}\nResponse: {response.json()}\n\n')

    # Send the ChatGPT API's response to the user
    await message.answer(response.json()['choices'][0]['text'])

# Register the handle_message function as a handler for text messages
dp.register_message_handler(handle_message, content_types=types.ContentType.TEXT)


# Start the bot:
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
