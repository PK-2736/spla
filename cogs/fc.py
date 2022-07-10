import discord
from discord.ext import commands
import asyncio
import random
import config
import os
from bs4 import BeautifulSoup as soup


class fc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.remove_command('help')  # remove default help command


    @commands.command()  # set fc
    async def fcset(self, ctx, *, friendcode):
        discordname = ctx.message.author.id
        file = open("data/friendcodes.txt", "a")  # a is for "appending" aka adding text to the document
        # writes users @ and fc
        file.write(f'<@{discordname}> ')
        file.write(f'{friendcode}\n')
        file.close()  # closes the opened txt file
        await ctx.send(f'<@{discordname}> フレンドコードを設定しました {friendcode}')  # this lets the bot speak

    #kelly request to show all fc at once
    @commands.command()  # set fc for names
    async def fcall(self, ctx):
        searchfile = open("data/friendcodes.txt", "r")
        ayee = searchfile.readlines()
        searchfile.close()
        await ctx.author.send(ayee)

    async def fctwo(self, ctx):
        with open('data/friendcodes.txt', 'r') as f:
            for line in f:
                await ctx.author.send(line)
                if 'str' in line:
                    break


    @commands.command() #finds friendcodes
    async def fcfind(self, ctx, member):
        searchfile = open("data/friendcodes.txt", "r")
        member = member.replace('!', '')  # this allows people that have nicknames on discord to be found, by replacing
        # the ! discord puts in your id with nothing thus deleting the ! (thanks alex!)
        print(member)
        for line in searchfile:
            if f'{member}' in line:
                print(member)
                print(line)
        await ctx.send(f"フレンドコード -> {line}")
        searchfile.close()


    # with is an efficient way of opening a file so it can be used,
    # setting the open object to a variable (in this case "f"), and closing the file
    @commands.command()  # remove fc's
    async def fcremove(self, ctx, member, fc):  # discord @ and friend code are required attributes <- right word? idk
        with open("data/friendcodes.txt", "r") as f:
            lines = f.readlines()  # This method returns a list containing the lines
            # to test if its working
            print(lines)
            print(member)
            print(fc)
        with open("data/friendcodes.txt", "w") as f:  # opens the text file again to delete text
            for line in lines:
                if line.strip(" \n") != f'{member} {fc}':  # deletes @ if its found and deletes
                    f.write(line)  # write all the other fc's
            await ctx.send(f"poof! it's gone!")

def setup(bot):
    bot.add_cog(fc(bot))