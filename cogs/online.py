from nextcord.ext import commands
from data import guild_id
class online(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def online_event(self):
    print("I'm online")
    for channel in self.bot.get_guild(guild_id).channels:
      await channel.edit(slowmode_delay=5)

def setup(bot):
  bot.add_cog(online(bot))
