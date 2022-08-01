from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None)
from os import listdir, system
from data import token
from host import Host
Host()
for fn in listdir('cogs'):
  if fn.endswith(".py"):
    bot.load_extension(f'cogs.{fn[:-3]}')
try:
  bot.run(token)
except Exception as e:
  print(e)
  system('kill 1')
