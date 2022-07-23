from discord.ext import commands
import discord
from discord.commands import slash_command, Option

print("helpの読み込み完了")

class uihelp(discord.ui.View):
    @discord.ui.select(
        placeholder="ココをタップ",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="スプラコマンド"),
            discord.SelectOption(label="フレンドコードコマンド"),
            discord.SelectOption(label="募集コマンド"),
            discord.SelectOption(label="読み上げコマンド"),
            discord.SelectOption(label="音楽コマンド"),
            discord.SelectOption(label="その他コマンド"),
        ],
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "スプラコマンド":
            embed = discord.Embed( 
                          title="スプラコマンド",
                          color=0x76d8be, 
                          url="https://example.com"
                          )
            embed.add_field(name='/spla S2(r(レギュラー), g(ガチマッチ), l(リーグマッチ), s(サーモンラン)', value='スプラ2のステージ表示')
            embed.add_field(name='武器', value='ランダムに武器を表示')
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "フレンドコードコマンド":
            embed = discord.Embed( 
                          title="フレンドコードコマンド",
                          color=0xe7ad5b, 
                          url="https://example.com"
                          )
            embed.add_field(name='/fc set (自分のフレンドコード）', value='フレンドコードを保存する')   
            embed.add_field(name='/fc find (対象の人をメンション)', value='フレンドコードを検索する') 
            embed.add_field(name='/fc remove (自分をメンション) (自分のフレンドコード)', value='自分のフレンドコードを削除する')         
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "募集コマンド":
            embed = discord.Embed( 
                          title="募集コマンド",
                          color=0xc376d8, 
                          url="https://example.com" 
                          )
            embed.add_field(name='BOTのメンションの後に時間 ルール 募集人数 募集内容を記入', value='```例：@splabot 21時から@1リグマ募集```')
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "読み上げコマンド":
            embed = discord.Embed( 
                          title="読み上げコマンド",
                          color=0x00ff00, 
                          url="https://example.com"
                          )
            embed.add_field(name='読み上げを開始', value='!talk,?talk')
            embed.add_field(name='読み上げ終了', value='!stop,?stop')              
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "音楽コマンド":
            embed = discord.Embed( 
                          title="音楽コマンド",
                          color=0xe75b5b, 
                          url="https://example.com"
                          )
            embed.add_field(name='!help', value='音楽コマンドのhelp')
            embed.add_field(name='!play (流したい曲URLor曲名)', value='曲を再生します')
            await interaction.response.edit_message(embed=embed)

        elif select.values[0] == "その他コマンド":
            embed = discord.Embed( 
                          title="その他コマンド",
                          color=0xdfdd1d, 
                          url="https://example.com"
                          )
            embed.add_field(name='/help', value='実行しているコマンド')
            embed.add_field(name='/client_info', value='BOTの情報を表示')
            embed.add_field(name='/client_application_info', value='BOTの情報を表示2')
            await interaction.response.edit_message(embed=embed)

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @slash_command(guild_ids=[981474117020712970], description="コマンドのHELPを表示します")
    async def help(self, ctx):
            await ctx.respond(f"{ctx.author.mention} コマンド一覧です", view=uihelp())

def setup(bot):
    bot.add_cog(help(bot))