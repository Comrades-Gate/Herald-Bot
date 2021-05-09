import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext import commands

theKey = os.environ['TOKEN'] # Encrypted bot invocation token.

### Set bot prefix.
bot = commands.Bot(command_prefix='/hb')

### Connect to Discord.
@bot.event
async def on_ready():
  print(f'{bot.user.name} is now online.')

### Functions called by command functions.
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " **- "+ json_data[0]['a'] + "**"
  return quote

### Command functions paired to /hb
@bot.command()
async def suggest(ctx, *, arg):
  embed = discord.Embed(title='Herald Bot Suggestions', description=f'Submitted by: {ctx.author.mention}', color=discord.Color.green())
  embed.add_field(name='Suggestion', value=arg)
  channel = ctx.guild.get_channel(840961608166801458)
  msg = await channel.send(embed=embed)
  await msg.add_reaction('👍') # yea
  await msg.add_reaction('👎') # nay
  await ctx.message.delete()
@suggest.error # Command-specific error message.
async def suggest_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('```/hbsuggest <your_suggestion> \n           ^^^^^^^^^^^^^^^^^\n\n<your_suggestion> is a required argument!```')

@bot.command()
async def quote(message):
  q = get_quote()
  await message.channel.send(q)

starter_encouragements = ["Hang in there!","You are precious cargo!","I think you're pretty great!","ily <3","You can do it booboo!","I am rooting for you!"]
@bot.command()
async def isad(message):
  await message.channel.send(random.choice(starter_encouragements))

### General error-handling response.
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('`Code 0 - Command does not exist.`')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('`Code 1 - Missing a required argument.`')
  else:
    await ctx.send('`Code 216 - Unknown error code. Embrace the mystery, my friend!`')


### Turn the bot on.
keep_alive()
theKey = os.environ['TOKEN']
bot.run(theKey)