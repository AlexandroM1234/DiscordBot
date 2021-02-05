import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
TOKEN = os.getenv("TOKEN")
tracker = {}


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.content.startswith("$hello"):
        await message.channel.send("Hello gentlemen I'm the StatTrak Bot")


client.run(TOKEN)
