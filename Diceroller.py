import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '=')

@client.event
async def on_ready():
	print("Lets F-ing gooooo")

@client.command(aliases=['roll'])
async def rolls(ctx, num):
    input = int(num)
    roll = random.randint(1, input)
    await ctx.send(f'Gamer rolled {roll}')

client.run('Insert Bot Token here')