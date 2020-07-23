import discord

from discord.ext.commands import (
	Cog,
	CommandOnCooldown,
	MissingPermissions,
	CommandInvokeError,
	CommandNotFound, 
	MissingAnyRole,
	BadArgument,
	NotOwner)
from math import ceil

class Handler(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.color = 0xFF0000

	@Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, CommandOnCooldown):
			return await ctx.send(embed=discord.Embed(color=self.color, timestamp=ctx.message.created_at, description="%s, Please wait %ss to use this command again."%(ctx.author.mention, ceil(error.retry_after))))
		if isinstance(error, (MissingPermissions, MissingAnyRole)):
			return await ctx.send(embed=discord.Embed(color=self.color, timestamp=ctx.message.created_at, description="%s, You do not have permissions to use this Command!" %(ctx.author.mention)))
		if isinstance(error, CommandInvokeError):
			return await ctx.send(embed=discord.Embed(color=self.color, timestamp=ctx.message.created_at, description="%s, Unexpected error invoking this command, sorry. ```py\n%ss\n```" %(ctx.author.mention, (error))))
		if isinstance(error, BadArgument):
			return await ctx.send(embed=discord.Embed(color=self.color, timestamp=ctx.message.created_at, description="%s, I didn't find this user." % ctx.author.mention))
		if isinstance(error, NotOwner):
			return await ctx.send(embed=discord.Embed(color=self.color, timestamp=ctx.message.created_at, description="%s, somente o <@296428519947370499> pode executar esse comando." % ctx.author.mention))

def setup(bot):
	bot.add_cog(Handler(bot))