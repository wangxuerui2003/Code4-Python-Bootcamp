import discord
import dotenv
from pathlib import Path
import os
import sys

intents = discord.Intents.default()
intents.message_content = True

# Load .env file
dotenv_path = Path('../../.env')
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Get discord bot token
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
	print("TOKEN does not exist in environment!", file=sys.stderr)
	sys.exit()


# Run discord bot
client = discord.Client(intents=intents)

@client.event
async def on_connect():
	print("Bot connected to server!")

@client.event
async def on_ready():
	print("Logged in as", client.user)

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('$hello'):
		await message.channel.send("Hello World!")

client.run(TOKEN)