import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext import commands

my_secret = os.environ['TOKEN'] # Encrypted bot invocation token.

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " **- "+ json_data[0]['a'] + "**"
  return quote

bot = commands.Bot(command_prefix='/hb')

@bot.event
async def on_ready():
  print(f'{bot.user.name} is now online.')

@bot.command()
async def suggest(ctx, *, arg):
  embed = discord.Embed(title='Herald Bot Suggestions', description=f'Submitted by: {ctx.author.mention}', color=discord.Color.green())
  embed.add_field(name='Suggestion', value=arg)
  channel = ctx.guild.get_channel(840961608166801458)
  msg = await channel.send(embed=embed)
  await msg.add_reaction('👍') # yea
  await msg.add_reaction('👎') # nay
  await ctx.message.delete()

@bot.command()
async def quote(message):
  q = get_quote()
  await message.channel.send(q)

starter_encouragements = ["Hang in there!","You are precious cargo!","I think you're pretty great!","ily <3","You can do it booboo!","I am rooting for you!"]
@bot.command()
async def isad(message):
  await message.channel.send(random.choice(starter_encouragements))

keep_alive()
my_secret = os.environ['TOKEN']
bot.run(my_secret)