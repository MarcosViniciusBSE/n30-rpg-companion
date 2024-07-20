import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

from models.roll import Roll
from models.help import Help

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-N30 ',help_command=None, intents=intents)


@bot.event
async def on_ready():
    print('{0.user} has started'.format(bot))


@bot.event
async def on_message(message):
    print(f"Mensagem recebida: {message.content}")
    await bot.process_commands(message)


@bot.command()
async def oi(ctx):
    await ctx.send("Oi! Eu sou Neo!")


@bot.command()
async def roll(ctx, arg):
    roll = Roll(arg)
    await ctx.send(roll.rollDice())


@bot.command(name="help")
async def custom_help(ctx, arg):
    help = Help(arg)
    await ctx.send(help.get_Help())


bot.run(os.getenv('TOKEN'))
