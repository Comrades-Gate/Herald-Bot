import discord
import os
import requests
import json
import random
from typing import Optional
from datetime import datetime
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions

intents = discord.Intents().all() # Allows the bot to collect user data.
theKey = os.environ['TOKEN'] # Encrypted bot invocation token.

### Set bot prefix.
bot = commands.Bot(command_prefix='/hb ', intents=intents)

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
# /hb isad
@bot.command()
async def isad(message):
  encouragements = ["Hang in there!","You are precious cargo!","I think you're pretty great!","ily <3","You can do it booboo!","I am rooting for you!"]
  await message.channel.send(random.choice(encouragements))

#/hb memberlist
@bot.command(aliases = ['ml', 'mlist'])
@commands.has_permissions(administrator=True)
#@commands.has_role(ROLE_ID)
async def memberlist(ctx):
  mlist = ctx.guild.members
  users = "\n".join([(member.name + "#" + member.discriminator) for member in mlist])
  user_ids = "\n".join([str(member.id) for member in mlist])
  embed = discord.Embed(title=f'Member list for {ctx.guild.name}',
  description = "This list includes **all** members in the server.", color = discord.Color.blue())
  embed.add_field(name="Discord User", value=users)
  embed.add_field(name="User ID", value=user_ids)
  await ctx.send(embed=embed)

#/hb myrole
@bot.command(aliases = ['mr'])
@commands.has_permissions(administrator=True)
async def myrole(ctx):
  await ctx.send(ctx.role.name)

# /hb quote
# This is one of the few functions that does not require the Context argument.
@bot.command(aliases = ['rq'])
async def quote(message):
  q = get_quote()
  await message.channel.send(q)

#/hb suggest
@bot.command(aliases = ['sug'])
async def suggest(ctx, *, arg):
  embed = discord.Embed(title='Herald Bot Suggestions', description=f'Submitted by: {ctx.author.mention}', color=discord.Color.green())
  embed.add_field(name='Suggestion', value=arg)
  channel = ctx.guild.get_channel(842076296133083150) #840961608166801458 for main Discord.
  msg = await channel.send(embed=embed)
  await msg.add_reaction("⬆️") # yea👍
  await msg.add_reaction("⬇️") # nay👎
  await ctx.message.delete()
@suggest.error # Command-specific error message.
async def suggest_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('```/hbsuggest <your_suggestion> \n           ^^^^^^^^^^^^^^^^^\n\n<your_suggestion> is a required argument!```')

### General error-handling response.
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('`Code 0: Command does not exist.`')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('`Code 1: Missing a required argument.`')
  elif isinstance(error, commands.BadArgument):
    await ctx.send('`Code 2: Bad argument.`')
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.message.delete()
    await ctx.send('`Code 3: Cooldown time on command has not expired.`')
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send('`Code 4: User has insufficient permissions.`')
  elif isinstance(error, commands.BotMissingPermissions):
    await ctx.send('`Code 5: Bot has insufficient permissions.`')
  elif isinstance(error, commands.MissingRole):
    await ctx.send('`Code 6: User has insufficient roles.`')
  elif isinstance(error, commands.BotMissingRole):
    await ctx.send('`Code 7: Bot has insufficient roles.`')
  else:
    await ctx.send('`Code 216: Unknown error code. Embrace the mystery, my friend!`')


### Turn the bot on.
keep_alive()
theKey = os.environ['BETA_TOKEN']
bot.run(theKey)
