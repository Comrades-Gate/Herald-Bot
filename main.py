import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing", "fml", "kms"]

starter_encouragements = [
  "Hang in there!",
  "You are precious cargo!",
  "I think you're pretty great!",
  "ily <3"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
    print('{0.user} is now online.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('/help'):
        await message.channel.send('IM NOT FINISHED YET')
    
    if msg.startswith('/quote'):
      quote = get_quote()
      await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice
      (starter_encouragements))

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)