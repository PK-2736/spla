from discord.ext import commands
import discord
import asyncio
from discord.commands import slash_command, Option

print("clientの読み込み完了")

class client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(guild_ids=[981474117020712970], description="BOTのステメ変更")
    async def client_change_presense(self, ctx, title):
        client = self.bot
        game = discord.Game(name=title)
        await client.change_presence(activity=game)

    @commands.is_owner()
    @commands.command(guild_ids=[981474117020712970], description="BOTをシャットダウン")
    async def client_close(self, ctx):
        client = self.bot
        await ctx.respond("Botアカウントからログアウトします。")
        await client.close()
        
    @slash_command(guild_ids=[981474117020712970], description="BOTの情報表示2")
    async def client_info(self, ctx):
        client = self.bot
        await ctx.respond(
            f"Botユーザー名: {client.user.name}\n"
            f"BotユーザーID: {client.user.id}\n"
            f"Guild数: {len(client.guilds)}\n"
            f"ボイス接続数: {len(client.voice_clients)}\n"
            f"ユニークユーザー数: {len(client.users)}\n"
            f"延べユーザー数: {sum([g.member_count for g in client.guilds])}\n"
        )

    @slash_command(guild_ids=[981474117020712970], description="BOTの情報表示")
    async def client_application_info(self, ctx):
        client = self.bot
        app_info = await client.application_info()
        await ctx.respond(
            f"アプリケーションID: {app_info.id}\n"
            f"Botオーナー: {app_info.owner.name}\n"
            f"Public Bot?: {app_info.bot_public}\n"
        )
        
def setup(bot):
    bot.add_cog(client(bot))