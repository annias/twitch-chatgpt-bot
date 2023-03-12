from revChatGPT.V3 import Chatbot
import json

with open("config.json", "r") as k:
    config = json.load(k)

bot = Chatbot(api_key=config['openAI_API'], engine="gpt-3.5-turbo")

async def handle_response(message) -> str:
    return bot.ask(message)
