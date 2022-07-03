from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.remove_command('help')


    @commands.command(pass_context=True)  # new help command
    async def help(self, ctx):
        # formats the help description so is looks nice neat and a bit colorful
        embed = discord.Embed(
            color=discord.Color.gold()  # makes the line on the side gold
        )

        # name is for the title font and value is the description font
        # inline doesnt really do anything as far as I know
        embed.add_field(name='.help', value='It\'このボットのコマンド一覧', inline=False)
        embed.add_field(name='.fcset', value='自分のフレンドコードを保存　例 (.fcset 6550-2620-9043)', inline=False)
        embed.add_field(name='.fcfind', value='自分のフレンドコード。相手のフレンドコードを検索　例 (.fcfind @PheyK)'
                        , inline=False)
        embed.add_field(name='.fcremove', value='自分の保存したフレンドコードを削除 '
                                            'フレンドコードを含める必要があります。 '
                                            '(.fcremove @PheyK 6550-2620-9043)', inline=False)
        embed.add_field(name='.bs', value='マルチメンバー募集コマンド '
                                              '例 (.bs 本日21時からの4人リーグマッチ募集)',
                        inline=False)
        embed.add_field(name='!talk,?talk', value='読み上げbot開始 (このbotとは別のbotが反応します）', inline=False)

        await ctx.author.send(embed=embed)  # this will dm you the text above

def setup(bot):
    bot.add_cog(help(bot))