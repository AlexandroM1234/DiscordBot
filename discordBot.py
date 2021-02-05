import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
TOKEN = os.getenv("TOKEN")

tracker = {
    "aj being too hot": 1000,
    "aj being too cold": 10,
    "alex's dead horses": 3,
    "times dom noticed the new bot": 1,
}


def create(msg):
    newTracker = msg.split(">create", 1)[1]
    if newTracker not in tracker:
        tracker[newTracker] = 1
        return f"New Tracker made, {newTracker} = {tracker[newTracker]}"

    else:
        f"That tracker is already made, {newTracker} = {tracker[newTracker]}"


@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_message(message):
    msg = message.content
    if msg.startswith(">create"):
        newTracker = create(msg)
        await message.channel.send(newTracker)

    if msg.startswith(">show all"):
        for keys in tracker:
            await message.channel.send(f"{keys} = {tracker[keys]}")


client.run(TOKEN)