import discord
from discord.ext import commands
from discord.commands import slash_command, Option

print("serverhelpの読み込み完了")

class serverhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    # 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
    async def on_ready(self): 
        embed = discord.Embed( # Embedを定義する
                          title="splabotの使い方",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          )
        #embed.add_field(name="スプラコマンド",value="スプラ2のステージ表示：スプラコマンド, s(サーモンラン))を指定\n"
                            #"ランダムに武器を表示：武器")
        #embed.add_field(name="フレンドコードコマンド",value="フレンドコードを保存する：/fc set (自分のフレンドコード）\n"
        #"フレンドコードを検索する：/fc find (対象の人をメンション)\n"
        #"/fc remove (自分をメンション) (自分のフレンドコード)：/fc remove (自分をメンション) (自分のフレンドコード)")
        #embed.add_field(name="募集コマンド",value="BOTのメンションの後に'時間' 'ルール' '募集人数' '募集内容'を記入\n"
        #"例：```例：@splabot 21時から@1リグマ募集```")
        #embed.add_field(name="読み上げコマンド",value="読み上げを開始：!talk,?talk"
        #"\n!talk,?talk：!stop,?stop\n※このコマンドは別のBOTが反応します")
        #embed.add_field(name="音楽コマンド",value="BOTを指定したボイスチャンネルに接続：/music connect (ボイスチャンネルID)\n"
        #"指定した曲を再生、またはキューに追加：music play (自分の流したい曲のURL)\n"
        #"現在流している曲名を表示：/music now_playing\n"
        #"キューに入っている曲を表示します：/music queue\n"
        #"曲を一時停止します：/music pause\n曲を再生します：/music resume\n"
        #"曲をスキップします：/music skip"
        #"\n音のボリュームを変更します：/music volume (ボリュームの数値)\n"
        #"ボイスチャンネルからBOTを退出させます：/music stop")
        #embed.add_field(name="その他コマンド",value="簡易HELPを表示：/help\n"
        #"BOTの情報を表示：/client_info\n"
        #"BOTの情報を表示2：/client_application_info")
        embed.add_field(name='```スプラコマンド```', value='----------', inline=False)
        embed.add_field(name='/spla S2(r(レギュラー), g(ガチマッチ), l(リーグマッチ), s(サーモンラン)', value='スプラ2のステージ表示', inline=True)
        embed.add_field(name='武器', value='ランダムに武器を表示', inline=True)
        embed.add_field(name='```フレンドコードコマンド```', value='----------', inline=False)
        embed.add_field(name='/fc set (自分のフレンドコード）', value='フレンドコードを保存する', inline=True)
        embed.add_field(name='/fc find (対象の人をメンション)', value='フレンドコードを検索する', inline=True)
        embed.add_field(name='/fc remove (自分をメンション) (自分のフレンドコード)', value='自分のフレンドコードを削除する', inline=True)
        embed.add_field(name='```募集コマンド```', value='----------', inline=False)
        embed.add_field(name='BOTのメンションの後に時間 ルール 募集人数 募集内容を記入', value='```例：@splabot 21時から@1リグマ募集```', inline=True)
        embed.add_field(name='```読み上げコマンド```', value='----------', inline=False)
        embed.add_field(name='読み上げを開始', value='!talk,?talk', inline=True)
        embed.add_field(name='読み上げ終了', value='!stop,?stop', inline=True)
        embed.add_field(name='```音楽コマンド```', value='----------', inline=False)
        embed.add_field(name='音楽コマンドのhelp', value='!help', inline=True)
        embed.add_field(name='曲を再生', value='!play (流したい曲URLor曲名)', inline=True)
        embed.add_field(name='```その他コマンド```', value='----------', inline=False)
        embed.add_field(name='/help', value='コマンド別help表示', inline=True)
        embed.add_field(name='/client_info', value='BOTの情報を表示', inline=True)
        embed.add_field(name='/client_application_info', value='BOTの情報を表示2', inline=True)
        embed.add_field(name="=============================",value="**見にくくなってしまったので、なんとなく確認してスラッシュコマンドのガイドを使って下さい！**",inline=False)

        guild = self.bot.get_guild(981474117020712970)
        channel = guild.get_channel(982600408704892998)

        await channel.send(embed=embed) # embedの送信には、embed={定義したembed名}

def setup(bot):
    bot.add_cog(serverhelp(bot))