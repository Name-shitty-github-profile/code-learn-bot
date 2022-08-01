from buttons import ticketbtn
from nextcord.ext import commands
import nextcord
from data import guild_id

class ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def ticketchannel(self):
    view = ticketbtn()
    channel = self.bot.get_channel(1003489907358060544)
    await channel.purge(limit=1)
    await channel.send(embed=nextcord.Embed(title="Ticket", description="Tout ticket inutile sera sanctionné.\n\nVeuillez ne pas faire un ticket pour demander de l'aide, veuillez plutot aller dans la section aide.", color=0x2ecc71), view=view)
    await view.wait()

  @nextcord.slash_command(name = "ticket", description = "Utilise cette commande pour créer un ticket ou va dans le salon ticket !", guild_ids=[guild_id])
  async def ticketslash(self, interaction: nextcord.Interaction):
    view = ticketbtn()
    await interaction.response.send_message("Voici le boutton pour créer un ticket", ephemeral=True, view=view)
    await view.wait()

  @commands.command()
  async def close(self, ctx):
    if 1003489729301450894 not in [role.id for role in ctx.author.roles]: return
    await ctx.send('Laisse moi analyser tout cela avant ...')
    msglist = []
    async for message in ctx.channel.history(limit = 100): msglist.append(message)
    await ctx.channel.delete()
    channel = await ctx.guild.create_text_channel(f'archive-{ctx.channel.name}', category=ctx.guild.get_channel(1003489880686460928))
    msglist.reverse()
    for message in msglist: await channel.send(embed=nextcord.Embed(title=f'{message.author}', description=message.content, color = 0xe91e63).set_footer(text=message.created_at.__format__('%A, %d. %B %Y %H:%M:%S')))

def setup(bot):
  bot.add_cog(ticket(bot))
