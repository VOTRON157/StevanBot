import discord
from discord.ext import commands

class utils(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.cooldown(1,5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command()
  async def avatar(self, ctx, *, avamember : discord.Member=None):
    if avamember is None:
  
      await ctx.send('Please mention a user.')
      return
    if avamember == "":
      await ctx.send("I didn't find anyone, please use id's, mentions or usernames")
  
    await ctx.send(avamember.avatar_url) 
    
  @commands.cooldown(1,5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def say(self, ctx, *, palavra=None):
      if palavra is None:
        await ctx.send(f'<@{ctx.author.id}>, Type what I will say.')
        return
      await ctx.send(f'{palavra}')
  
  @commands.cooldown(1,5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command()
  async def help(self, ctx):
   utils = self.client.get_cog('utils')
   UtilsCommands = utils.get_commands()
   embed=discord.Embed(color=0x00b500, description=f"My current prefix is: `@StevanBot`")
   embed.set_author(name="Stevanbot | Help commands", icon_url=self.client.user.avatar_url)
   embed.set_thumbnail(url=self.client.user.avatar_url)
   embed.add_field(name="• Utility Commands", value=f'`{" ` | ` ".join([c.qualified_name for c in UtilsCommands])}`', inline=False)
   
   await ctx.send(embed=embed)
   

   

def setup(client):
  client.add_cog(utils(client))