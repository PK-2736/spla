import discord
import asyncio
from discord.ext import commands

print("eventの読み込み完了")

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            client = self.bot
            await client.change_presence(activity = discord.Activity(name="Help:/help", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="splatoon3", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            joinserver=len(client.guilds)
            servers=str(joinserver)
            await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="botについての連絡はPheyK#1280", type=discord.ActivityType.playing))
            await asyncio.sleep(15)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(981474117020712970)
        channel = guild.get_channel(982580316894015530)
        embed = discord.Embed( # Embedを定義する
                        title=f"{member.name}が入室しました！",# タイトル
                        description="まずは #ルール を呼んで自己紹介を書きましょう！",
                        color=0x00ff00,) # フレーム色指定(今回は緑)
        meg = await channel.send(embed=embed)
        await meg.add_reaction("👍")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = self.bot.get_guild(981474117020712970)
        channel = guild.get_channel(982596256868225054)
        await channel.send(f"{member.name}行かないで！どうしてなの！？ 私を置いていかないで！")

def setup(bot):
    bot.add_cog(event(bot))