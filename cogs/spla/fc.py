import discord
from discord import SlashCommand, Option
from discord.ext import commands

print("fcの読み込み完了")

class fc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    guild_ids = [981474117020712970]  

    fc = discord.SlashCommandGroup("fc", "フレンドコード関連", guild_ids = guild_ids)

    @fc.command(description="自分のフレンドコードをセットします")
    async def set(self, ctx, *, friendcode: Option(str, "例：1111-1111-1111")):
        discordname = ctx.author.mention
        file = open("data/friendcodes.txt", "a")
        file.write(f'<@{discordname}> ')
        file.write(f'{friendcode}\n')
        file.close()
        await ctx.respond(f'<{discordname}> フレンドコードを設定しました {friendcode}')

    @commands.is_owner()
    @fc.command(description="登録されている全てのフレンドコード表示します(管理者向け)")
    async def all(self, ctx):
        searchfile = open("data/friendcodes.txt", "r")
        ayee = searchfile.readlines()
        searchfile.close()
        await ctx.author.respond(ayee)

    async def two(self, ctx):
        with open('data/friendcodes.txt', 'r') as f:
            for line in f:
                await ctx.author.respond(line)
                if 'str' in line:
                    break

    @fc.command(description="特定の人のフレンドコードを表示します")
    async def find(self, ctx, member: Option(str, "例：@PheyK")):
        searchfile = open("data/friendcodes.txt", "r")
        member = member.replace('!', '')
        print(member)
        for line in searchfile:
            if f'{member}' in line:
                print(member)
                print(line)
        await ctx.respond(f"フレンドコード->{line}")
        searchfile.close()


    @fc.command(description="登録しているフレンドコードを削除します")
    async def remove(self, ctx, member: Option(str, "例：@PheyK"), fc: Option(str, "例：1111-1111-1111")):
        with open("data/friendcodes.txt", "r") as f:
            lines = f.readlines()
            print(lines)
            print(member)
            print(fc)
        with open("data/friendcodes.txt", "w") as f:
            for line in lines:
                if line.strip(" \n") != f'{member} {fc}':
                    f.write(line)
            await ctx.respond(f"<フレンドコードを削除しました")

def setup(bot):
    bot.add_cog(fc(bot))