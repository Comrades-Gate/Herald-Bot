import os
import discord
from glob import glob
from datetime import datetime
from ..db import db
#from ..ping import keep_alive
from asyncio import sleep
from discord import Embed, File
from discord import Intents
from discord.errors import HTTPException, Forbidden
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown)
from discord.ext.commands import when_mentioned_or, command, has_permissions
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

SERVER_ID = 842072102769131570
OWNER_IDS = [265251249597841408]

COGS = []
for file in os.listdir("./lib/cogs"):
  if file.endswith(".py"):
    COGS.append(file)
#COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
IGNORE_EXCEPTIONS = (BadArgument)

def get_prefix(bot, message):
  db.field("SELECT Prefix FROM Guilds WHERE GuildID = ?", message.guild.id)
  return when_mentioned_or(prefix)(bot, message)

class Ready(object):
  def __init__(self):
    for cog in COGS:
      setattr(self, cog, False)
  
  def ready_up(self, cog):
    setattr(self, cog, True)
    print(f"{cog} cog ready.")
  
  def all_ready(self):
    return [getattr(self, cog) for cog in COGS]

class Bot(BotBase):
  def __init__(self):
    self.ready = False
    self.cogs_ready = Ready()
    self.guild = None
    self.scheduler = AsyncIOScheduler()
    db.autosave(self.scheduler)
    super().__init__(command_prefix=get_prefix, owner_ids=OWNER_IDS, intents=Intents.all())
  
  def setup(self):
    for cog in COGS:
      self.load_extension(f'lib.cogs.{cog[:-3]}')
      print (f"{cog} cog loaded.")
  
  def run(self, version):
    self.VERSION = version
    print ("Initializing Herald Bot...")
    self.setup()
    super().run(os.environ['BETA_TOKEN'], reconnect=True)
  
  async def process_commands(self, message):
    ctx = await self.get_context(message, cls=Context)
    print(ctx)
    
    if ctx.command is not None and ctx.guild is not None:
      if self.ready:
        await self.invoke(ctx)
      else:
        await ctx.send("Herald Bot is not ready to receive commands yet. Try again later!")

  async def on_connect(self):
    print("Herald Bot Status: CONNECTED")
  
  async def on_disconnect(self):
    print("Herald Bot Status: DISCONNECTED")
  
  async def on_error(self, err, *args, **kwargs):
    if err == "on_command_error":
      await args[0].send("Something went wrong.")
      raise
  
  async def on_command_error(self, ctx, exc):
    if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):
      pass
    elif isinstance(exc, MissingRequiredArgument):
      await ctx.send('`Code 1: Missing a required argument.`')
    elif isinstance(exc, BadArgument):
      await ctx.send('`Code 2: Bad argument.`')
    elif isinstance(exc, CommandOnCooldown):
      await ctx.message.delete()
      await ctx.send('`Code 3: Cooldown time on command has not expired.`')
    elif isinstance(exc, MissingPermissions):
      await ctx.send('`Code 4: User has insufficient permissions.`')
    elif isinstance(exc, BotMissingPermissions):
      await ctx.send('`Code 5: Bot has insufficient permissions.`')
    elif isinstance(exc, MissingRole):
      await ctx.send('`Code 6: User has insufficient roles.`')
    elif isinstance(exc, BotMissingRole):
      await ctx.send('`Code 7: Bot has insufficient roles.`')
    elif hasattr(exc, "original"):
      if isinstance(exc.original, Forbidden):
        await ctx.send("I do not have permission to do that!")
      else:
        raise exc.original
    else:
      raise exc

  #async def print_message(self):
    #channel = self.get_channel(842072104902852637)
    #await channel.send("This is a timed notification.")

  async def on_ready(self):
    if not self.ready:
      self.guild = self.get_guild(SERVER_ID)
      self.stdout = self.get_channel(842378888474001429)
      #self.scheduler.add_job(self.print_message, CronTrigger(second="0,15,30,45"))
      #self.scheduler.start()

      while not self.cogs_ready.all_ready():
        await sleep(0.5)

      # Notify the Bot Status channel on the development server.
      embed = Embed(description="Herald Bot is now **online** 🟢", color=0x00FF00, timestamp=datetime.utcnow())
      await self.stdout.send(embed=embed)
      self.ready = True
      print ("Herald Bot Status: READY")

    else:
      print ("WARNING: Herald Bot reconnecting!")
      await self.stdout.send("🟡 Herald Bot is attempting to **reconnect**...")

  async def on_message (self, message):
    if not message.author.bot:
      await self.process_commands(message)

#keep_alive()
bot = Bot()