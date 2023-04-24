import discord
import dotenv
from pathlib import Path
import os

typos = ['Twddy', 'Taddy', 'Trddy', 'Tnddy', 'Tmddy']

intents = discord.Intents.default()
intents.message_content = True

dotenv.load_dotenv(dotenv_path=Path("../../.env"))
TOKEN = os.getenv('TOKEN')


client = discord.Client(intents=intents)

@client.event
async def on_connect():
	print("Bot connected!")

@client.event
async def on_ready():
	print(f"Logged in as \"{client.user.display_name}\"")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content == '$hello':
		await message.reply("Hello World!")
	elif message.content == '$greet':
		await message.reply(f'Hello {message.author.name}!')
	elif message.content == '$greetings':
		await message.reply(f'Hello {message.author.display_name}!')
	else:
		if any(word in typos for word in message.content.split(' ')):
			await message.reply("Did you mean Teddy?")

client.run(TOKEN)