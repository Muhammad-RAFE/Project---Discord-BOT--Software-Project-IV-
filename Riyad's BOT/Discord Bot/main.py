import discord
import random
import time
import asyncio

TOKEN = "ODI4MTYxNDM3MjU1NTk4MTEy.YGljcQ.7gHt8sF2HoElM1pW6pHpUrKYb80"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".hi"):
        await message.channel.send("Hey, what’s up?")

    if message.content.startswith(".rules"):
            await message.channel.send("1. We're all in this together to create a welcoming environment. Let's treat everyone with respect. Healthy debates are natural, but kindness is required.\n2. Make sure everyone feels safe. Bullying of any kind isn't allowed, and degrading comments about things like race, religion, culture,  identity will not be tolerated.\n3. Being part of this group requires mutual trust. Authentic, expressive discussions make groups great, but may also be sensitive and private. What's shared in the group should stay in the group.\n")

    if message.content.startswith(".rakib"):
        await message.channel.send("Rakib is a very good boy. \nHis social activities are given below\n\n******FACEBOOK******\nhttps://www.facebook.com/rakib.zaman.100\n\n******INSTAGRAM******\nhttps://www.instagram.com/__.rakibb.__/")

    if message.content.startswith(".niloy"):
        await message.channel.send("Niloy is a very good boy.\nHis social activities are given below\n\n******FACEBOOK******\nhttps://www.facebook.com/asifiqbal.niloy.54\n\n******INSTAGRAM******\nhttps://www.instagram.com/niloyasifiqbal/")


    if message.content.startswith(".riyad"):
        await message.channel.send("Riyad is a good boy.\nHis social activities are given below\n\n******FACEBOOK******https://www.facebook.com/reallyhunter.riyad\n\n******INSTAGRAM******\nhttps://www.instagram.com/tamim_rahman_riyad/")

    if message.content.startswith(".rafe"):
        await message.channel.send("Rafe is a good boy\nhttps://www.facebook.com/rafeul.islam.3")

    if message.content.startswith(".ping"):
        await message.channel.send("pong")

    if message.content.startswith(".how are you"):
        await message.channel.send("Pretty good")


    if message.content.startswith(".mafia gaming"):
        await message.channel.send("here is link\nhttps://discord.gg/BKaEMbb")

    if message.content.startswith(".good evening"):
        await message.channel.send("Good evening! I hope you had a good and productive day. Cheer up!")

    if message.content.startswith(".good morning"):
        await message.channel.send("Hey, sleepyhead, have a great day!")

    if message.content.startswith(".chill"):
        await message.channel.send("“Oh, just chilling ”")

    if message.content.startswith(".goodbye"):
        await message.channel.send("The World will come to an end,as I say goodbye to my friend.But I khow I will pull through thos pain,beacues I know we'll meet again.Goodbye")

@client.event
async def on_ready():
    print("Running")


client.run(TOKEN)
print(client.user.name)

