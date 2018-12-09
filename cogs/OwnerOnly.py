import discord
import json
import sqlite3
from io import StringIO
from discord.ext import commands

conn = sqlite3.connect('configs/QuoteBot.db')
c = conn.cursor()

with open('configs/config.json') as json_data:
	response_json = json.load(json_data)

owners = response_json['owner_ids']
success_string = response_json['response_string']['success']
del response_json

class Owneronly:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def shutdown(self, ctx):
		if ctx.author.id in owners:
			await ctx.send(content = success_string + ' **Shutting down.**')
			await self.bot.logout()


def setup(bot):
	bot.add_cog(Owneronly(bot))
