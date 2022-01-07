from replit import db
import os
import discord
import requests
import json
import random
from keep_alive import keep_alive
my_secret = os.environ['Key']

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "sed", "rip","Sad", "Depressed", "Unhappy", "Angry", "Miserable", "Depressing", "Sed", "Rip", "RIP"]

thanking = ["Thank","Thanks","thank","thanks"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
] 

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\n" + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete(index):
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
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello There!')
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if message.content.startswith('$help'):
    await message.channel.send('type "$hello" - for welcome message.\ntype "$inspire" - for motivational quote.\ntype "$add" <scentence> - for adding an encouraging statement.\ntype "$delete" <index> - for deleting an encouraging line.\ntype "$list" - for lising the custom encouraging messages.\ntype "$help" - for help\n\nIt encourages you if you send a sad message.\n\nHave Fun Exploring!')
  
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + [db.get_raw("encouragements")]
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))
  if any(word in msg for word in thanking):
      await message.channel.send('My pleasure!')
  
  if msg.startswith("$add"):
    encouraging_message = msg.split("$add ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  if msg.startswith("$delete"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$delete",1)[1])
      delete(index-1)
      encouragements = db.get_raw("encouragements")
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db.get_raw("encouragements")
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(my_secret)