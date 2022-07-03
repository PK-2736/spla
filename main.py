import discord
from discord.ext import commands
import asyncio
import random
import config
import os
from bs4 import BeautifulSoup as soup

intents = discord.Intents.all() #need to enable
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("起動成功!")
    print("Running on version: " + str(discord.__version__))
    print("    ________")
    print("Spla-server!")
    print("管理者PheyK")


@bot.event
async def on_member_join(member) :
    print(f"{member} has joined the server")

@bot.event
async def on_member_remove(member) :
    print(f"{member} has left the server")

@bot.command(aliases = ['showPing'])
async def ping(ctx) :
    await ctx.send(f"Ping: {round(1000 * bot.latency)}ms")
    print(f"{str(ctx.message.author)} asked for the Ping")


@commands.is_owner()
@bot.command()
async def reload(ctx, module_name):
        await ctx.send(f"モジュール{module_name}の再読み込みを開始します。")
        try:
            bot.reload_extension(module_name)
            await ctx.send(f"モジュール{module_name}の再読み込みを終了しました。")
        except (commands.errors.ExtensionNotLoaded, commands.errors.ExtensionNotFound,
                commands.errors.NoEntryPointError, commands.errors.ExtensionFailed) as e:
            await ctx.send(f"モジュール{module_name}の再読み込みに失敗しました。理由：{e}")
            return

@commands.is_owner()
@bot.command()
async def load(ctx, extension) :
    bot.load_extension(f'cogs.{extension}')

@commands.is_owner()
@bot.command()
async def unload(ctx, extension) :
    bot.unload_extension(f'cogs.{extension}')

# reads 'cogs' folder and finds all .py files

for filename in os.listdir('./cogs') :
    if filename.endswith('.py') :
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.token, reconnect=False)