from discord.ext import commands
import discord
import requests

class Moeda(commands.Cog):
    ''' Valor da moeda por simbolos '''
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="valormoeda", help="Envia o preco da moeda (Envie o simbolo da moeda desejada)")
    async def send_calc(self, ctx, coin):
        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}')
            data = response.json()
            price = data.get('price')
            if price:
                # await ctx.send(price)
                card = discord.Embed(
                    title='Valor:',
                    description=price,
                    color=0x00FF00
                )
                await ctx.send(embed=card)
            else:
                await ctx.send('erro')
        except Exception as e:
            await ctx.send('Ops... Deu um erro')
def setup(bot):
    bot.add_cog(Moeda(bot))