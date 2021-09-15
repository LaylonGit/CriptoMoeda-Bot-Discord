import os
from decouple import config
from discord.ext import commands

bot = commands.Bot('!')

def load_cogs():
    bot.load_extension('manager')
    # bot.load_extension('tasks.buscarnoticias')
    for command in os.listdir('commands'):
        if command.endswith('.py'):
            cog = command[:-3]
            bot.load_extension(f'commands.{cog}')
load_cogs()
TOKEN = config('TOKEN')
bot.run(TOKEN)