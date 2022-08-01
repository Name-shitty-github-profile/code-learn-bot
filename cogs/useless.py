from nextcord.ext import commands
class useless(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_message")
  async def hi(self, message):
    for word in ['hi', 'hello', 'bonjour', 'salut', 'bonsoir', 'coucou', 'cc', 'slt', 'bjr']:
      if message.content.lower().startswith(word):
        await message.add_reaction("👋")
        return None

def setup(bot):
  bot.add_cog(useless(bot))
