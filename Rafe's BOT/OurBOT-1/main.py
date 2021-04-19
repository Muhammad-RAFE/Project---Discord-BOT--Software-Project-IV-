import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive




import asyncio

from random import randint
from flask import Flask 
from threading import Thread




client = discord.Client()

sad_words = ["bad", "evil", "kill", "dog", "blood", "dead"]

starter_encouragements = [
  "Stop using bad word!",
  "Hang in there.",
  "I am calling ADMIN!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.gif)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)




def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")
  if message.author == client.user:
    return
  elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

  elif message.content.startswith('$ping'):
        await message.channel.send('Pong!')

  elif message.content.startswith('$howru'):
        await message.channel.send('I am Good  !')

  elif message.content.startswith('$whoru'):
        await message.channel.send('I am a BOT. I am a program !')

  elif message.content.startswith('$help'):
        await message.channel.send('1.$ping \n 2.$howru \n 3.$whoru \n  for help type  $help')
 


keep_alive()
client.run(os.getenv('TOKEN'))