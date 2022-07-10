import os
from re import M
import discord
import cogs.message_generator as mg
import asyncio
import time
from discord.ext import commands
import config

ATUMARU_BOT_ENV_DEV = "dev"
ATUMARU_BOT_ENV_PROD = "prod"
# 環境を確認
ATUMARU_BOT_ENV = (config.ATUMARU_BOT_ENV)
if ATUMARU_BOT_ENV != ATUMARU_BOT_ENV_DEV and ATUMARU_BOT_ENV != ATUMARU_BOT_ENV_PROD:
    raise "ATUMARU_BOT_ENV must be 'dev' or 'prod'"
ATUMARU_BOT_SEP = os.environ.get("ATUMARU_BOT_SEP")

def is_test_mode():
    "テストモードならばTrueを返却する"
    return ATUMARU_BOT_ENV == ATUMARU_BOT_ENV_DEV


def is_sep():
    "SEP向けならばTrueを返却する"
    return ATUMARU_BOT_SEP is not None

class bs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.remove_command('help')  # remove default help command

    @commands.Cog.listener()
    async def on_message(self, message):
        client = self.bot
        "メッセージが追加されたときに呼ばれる"
        if message.author == client.user:
            return
            # メッセージは前後の空白が自動で除去される
        content = message.content
            # 投稿文を作成する
        body, reaction_flag = mg.make_command_message(
                auther_menthon=message.author.mention,
                test_flag=is_test_mode(),
                content=content,
            )
            # 投稿文があれば投稿する
        if body is not None:
                message = await message.channel.send(body)
                # リアクションを必要に応じて付ける
                if reaction_flag:
                    await message.add_reaction("👍")
                    await message.add_reaction("🗑")
                    await message.add_reaction("🆗")

    async def on_reaction_update(self, reaction, user):
        client = self.bot
        "リアクションが追加または削除されたときに呼ばれる"
        message = reaction.message
            # Botが書いたメッセージに対して
        if message.author != client.user:
                return
            # 👍付けた人のメンション一覧
        user_mentions = []
            # 🗑付けた人のメンション一覧
        trash_user_mentions = []
            # 🆗付けた人のメンション一覧
        ok_user_mentions = []
            # メッセージについているリアクションをすべて取得
        for reaction in message.reactions:
                # リアクションのユーザ一覧
                async for user in reaction.users():
                    if user != client.user:
                        # Bot以外
                        if reaction.emoji == "👍":
                            user_mentions.append(user.mention)
                        elif reaction.emoji == "🗑":
                            trash_user_mentions.append(user.mention)
                        elif reaction.emoji == "🆗":
                            ok_user_mentions.append(user.mention)
            # 編集後メッセージ作成
        edited = mg.make_reaction_update_message(
                test_flag=is_test_mode(),
                content=message.content,
                user_mentions=user_mentions,
                trash_user_mentions=trash_user_mentions,
                ok_user_mentions=ok_user_mentions,
                sep_flag=is_sep(),
            )
        if edited == "":
                # 削除する
                await message.delete()
        elif edited is not None:
                # メッセージを編集する
                await message.edit(content=edited)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        "リアクションが追加されたときに呼ばれる"
        await self.on_reaction_update(reaction, user)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        client = self.bot
        "リアクションが削除されたときに呼ばれる"
        await self.on_reaction_update(reaction, user)
        return client

def setup(bot):
    bot.add_cog(bs(bot))