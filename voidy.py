import os
import discord
from discord.ext import commands

# Load your token from Railway's environment
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount + 1)  # +1 to remove the command message too

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
bot.run('MTM4ODg0MjMwOTYyMTEyNTI0MQ.GR33tr.EXt__SwgJhw9QjoJ-bimm7BNLro0lrWlv-8ugo')
