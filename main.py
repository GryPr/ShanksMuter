import datetime
import os
import discord
from discord.ext import commands

description = '''When you want Shanks to STFU'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(name='stfushanks', description='timeouts Shanks for a specific time')
async def stfu_shanks(ctx):
    shanks = await ctx.guild.fetch_member("751888799679774790")
    duration = datetime.timedelta(seconds=5)
    await shanks.timeout(duration, reason="SHUT THE FUCK UP")
    await ctx.send(f'It\'s joever for Shanks', ephemeral=True)


bot.run(os.environ['STUF_SHANKS_BOT_TOKEN'])