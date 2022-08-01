from nextcord.ext import commands
class anti(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_message")
  async def protect(self, message):
    if message.channel.name.startswith('ticket') or message.channel.id == 1003454684859744287 or any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in message.author.guild_permissions if p[1]])).lower() for word in ['admin']): return
    for word in ['https://', "discord.gg/"]:
      if word in message.content and len(message.content) > word:
        await message.delete()
        await message.author.send(f"Liens detecter !\n```\n{message.content}\n```")

def setup(bot):
  bot.add_cog(anti(bot))
