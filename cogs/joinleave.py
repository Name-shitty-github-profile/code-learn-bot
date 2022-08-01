from nextcord.ext import commands
from nextcord import Embed
class joinleave(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_member_join")
  async def welcome(self, member):
    await self.bot.get_channel(1003448652624302221).send(embed=Embed(title=f"Bienvenue {member.name} !", description="Je te suggère de lire le (règlement)[https://code-learn-tos.notnoemie.repl.co]", color=0x2ecc71))

  @commands.Cog.listener("on_member_remove")
  async def byebye(self, member):
    await self.bot.get_channel(1003799772869701682).send(embed=Embed(title=f"Aurevoir {member.name} !", description="Je te souhaite une bonne continuation dans la programmation!", color=0xe74c3c))

def setup(bot):
  bot.add_cog(joinleave(bot))
