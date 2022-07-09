from discord.ext import commands
import discord
import asyncio

class client(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        self.bot.remove_command('help')  # remove default help command

    @commands.is_owner()
    @commands.command()
    async def client_change_presense(self, ctx, title):
        client = self.bot
        game = discord.Game(name=title)
        await client.change_presence(activity=game)
    
    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            client = self.bot
            await client.change_presence(activity = discord.Activity(name="Help:.help", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            await client.change_presence(activity = discord.Activity(name="splatoon3", type=discord.ActivityType.playing))
            await asyncio.sleep(15)
            joinserver=len(client.guilds)
            servers=str(joinserver)
            await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
            await asyncio.sleep(15)

    @commands.is_owner()
    @commands.command()
    async def client_close(self, ctx):
        client = self.bot
        await ctx.send("Botアカウントからログアウトします。")
        await client.close()
        
    @commands.is_owner()
    @commands.command()
    async def client_info(self, ctx):
        client = self.bot
        await ctx.send(
            f"Botユーザー名: {client.user.name}\n"
            f"BotユーザーID: {client.user.id}\n"
            f"Guild数: {len(client.guilds)}\n"
            f"ボイス接続数: {len(client.voice_clients)}\n"
            f"ユニークユーザー数: {len(client.users)}\n"
            f"延べユーザー数: {sum([g.member_count for g in client.guilds])}\n"
        )

    @commands.is_owner()
    @commands.command()
    async def client_application_info(self, ctx):
        client = self.bot
        app_info = await client.application_info()
        await ctx.send(
            f"アプリケーションID: {app_info.id}\n"
            f"Botオーナー: {app_info.owner.name}\n"
            f"Public Bot?: {app_info.bot_public}\n"
        )

            
def setup(bot):
    bot.add_cog(client(bot))