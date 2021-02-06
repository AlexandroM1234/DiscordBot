import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


client = discord.Client()

tracker = {}


def showOne(msg):
    one = msg.split(">show ", 1)[1]
    try:
        return f"{one} = {tracker[one]}"
    except:
        return "That tracker doesn't exist"


def create(msg):
    newTracker = msg.split(">create ", 1)[1]
    if ">" in newTracker:
        return "> is not a valid character"
    if len(newTracker) == 0:
        return "You didnt give the tracker a name silly"
    if newTracker not in tracker:
        tracker[newTracker] = 1
        return f"New Tracker made, {newTracker} = {tracker[newTracker]}"

    else:
        f"That tracker is already made, {newTracker} = {tracker[newTracker]}"


def add(msg):
    text = msg.split(">add ", 1)[1]
    val = [int(char) for char in text.split() if char.isdigit()][0]
    key = " ".join(text.split(str(val), 1)[0].rsplit())

    try:
        tracker[key] += val
        return f"{key} = {tracker[key]}"
    except:
        return "That Tracker doesn't exist"


def remove(msg):
    text = msg.split(">remove ", 1)[1]
    val = [int(char) for char in text.split() if char.isdigit()][0]
    key = " ".join(text.split(str(val), 1)[0].rsplit())

    try:
        tracker[key] -= val
        return f"{key} = {tracker[key]}"
    except:
        return "That Tracker doesn't exist"


def delete(msg):
    one = msg.split(">delete ", 1)[1]
    try:
        del tracker[one]
        return f"{one} tracker deleted"
    except:
        return "That tracker doesn't exist"


@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_message(message):
    msg = message.content
    if msg.startswith(">create"):
        newTracker = create(msg)
        await message.channel.send(newTracker)

    if msg.startswith(">show"):
        singleTracker = showOne(msg)
        await message.channel.send(singleTracker)

    if msg.startswith(">add"):
        total = add(msg)
        await message.channel.send(total)

    if msg.startswith(">remove"):
        total = remove(msg)
        await message.channel.send(total)

    if msg.startswith(">delete"):
        deleteMessage = delete(msg)
        await message.channel.send(deleteMessage)

    if msg.startswith(">show all"):
        for keys in tracker:
            await message.channel.send(f"{keys} = {tracker[keys]}")


token = read_token()
client.run(token)