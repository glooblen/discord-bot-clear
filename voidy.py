import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount + 1)  # +1 to remove the command message too

bot.run('MTM4ODg0MjMwOTYyMTEyNTI0MQ.GR33tr.EXt__SwgJhw9QjoJ-bimm7BNLro0lrWlv-8ugo')