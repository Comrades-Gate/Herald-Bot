from random import choice, randint
from typing import Optional
from discord import Member
from ..db import db
from discord.ext.commands import Cog
from discord.ext.commands import command

class Fun(Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @command(name="hello", aliases=["hi", "hey"])
  async def say_hello(self, ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

  #def get_quote():
  #response = requests.get("https://zenquotes.io/api/random")
  #json_data = json.loads(response.text)
  #quote = json_data[0]['q'] + " **- "+ json_data[0]['a'] + "**"
  #return quote
  
  #@command(name="randomquote", aliases=["rq", "randq", "quote"], hidden=False)
  #async def rquote(message):
  #  q = get_quote()
  #  await message.channel.send(q)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("fun") #Pass filename not class name.
  
def setup(bot):
  bot.add_cog(Fun(bot))