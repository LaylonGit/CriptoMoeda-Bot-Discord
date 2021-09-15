from discord.ext import commands

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


class Manager(commands.Cog):
    ''' Falando com o usuario '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''Eu sou o {self.bot.user}''')
        # current_time.start()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "palavrão" in message.content:
            await message.channel.send(f'{message.author.name}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Envie todos os argumentos, digite !help')
        if isinstance(error, CommandNotFound):
            await ctx.send('Comando não existe, digite !help')
        else:
            raise error
def setup(bot):
    bot.add_cog(Manager(bot))
