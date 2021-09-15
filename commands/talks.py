from discord.ext import commands
import discord

class Talks(commands.Cog):
    ''' Falando com o usuario '''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="hello", help="Envia um hello para você (Não precisa enviar argumentos)")
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = 'Ola, ' + name
        await ctx.send(response)
    @commands.command(name="privado", help="Envia o mensagem no seu privado (Não precisa enviar argumentos)")
    async def send_calc(self, ctx):
        try:
            await ctx.author.send('Ola eu sou o bot do server')
        except discord.errors.Forbidden:
            await ctx.send('Ola talvez vc tenha desabilitado as mensagens privadas')
def setup(bot):
    bot.add_cog(Talks(bot))