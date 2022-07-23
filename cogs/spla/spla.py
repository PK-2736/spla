import discord
from discord.ext import commands
import asyncio
import random
import config
import os
from bs4 import BeautifulSoup as soup
from datetime import datetime, timedelta, timezone
import re
import requests
import json
import random
import logging
import time
import urllib
import urllib.request
from discord.commands import slash_command, Option

print("splaの読み込み完了")

def getJsonFromAPI(link):
    headers = {"User-Agent": "@murufon"}
    url = "https://spla2.yuu26.com/" + link
    response = requests.get(url,headers=headers)
    json_data = json.loads(response.text)
    return json_data

def getStageInfo(link, key, showRule=True):
    json_data = getJsonFromAPI(link)
    r = json_data['result']
    time_format = '%Y-%m-%dT%H:%M:%S'
    msg = f"{key}のスケジュールはこちら！\n"
    msg += "```\n"
    for i in range(3):
        start = datetime.strptime(r[i]['start'], time_format)
        end = datetime.strptime(r[i]['end'], time_format)
        msg += "\n" # markdownの最初の空行は無視される
        msg += f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}\n"
        if showRule:
            msg += f"{r[i]['rule']}\n"
        msg += f"{r[i]['maps'][0]}/{r[i]['maps'][1]}\n"
    msg += "```\n"
    return msg

def getCoopInfo(link, key):
    json_data = getJsonFromAPI(link)
    r = json_data['result']
    time_format = '%Y-%m-%dT%H:%M:%S'
    msg = f"{key}のスケジュールはこちら！\n"
    msg += "```\n"
    for i in range(2):
        start = datetime.strptime(r[i]['start'], time_format)
        end = datetime.strptime(r[i]['end'], time_format)
        msg += "\n"
        msg += f"{start.strftime('%m/%d %H:%M')} - {end.strftime('%m/%d %H:%M')}\n"
        msg += f"{r[i]['stage']['name']}\n"
        msg += f"{r[i]['weapons'][0]['name']}/{r[i]['weapons'][1]['name']}/{r[i]['weapons'][2]['name']}/{r[i]['weapons'][3]['name']}\n"
    msg += "```\n"
    return msg

def getDailyRandomString():
    JST = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(JST)
    now_str = str(now.strftime("%Y%m%d"))
    return now_str

class spl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    logging.basicConfig(level=logging.INFO)

    @commands.Cog.listener()
    async def on_message(self, message):
    # メッセージ送信者がBotだった場合は無視する
        if message.author.bot:
            return

        if message.content.lower() in ['buki', 'ぶき', 'ブキ', '武器', 'weapon', 'うえぽん', 'ウエポン']:
            json_open = open('data/weapon.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            buki = random.choice(json_data)
            ja_name = buki["name"]["ja_JP"]
            en_name = buki["name"]["en_US"]
            path = "images/main/" + buki["name"]["ja_JP"] + ".png"
            user = message.author.display_name
            await message.channel.send(f"{user}さんにおすすめのブキは{ja_name}({en_name})！" , file=discord.File(path))

        if message.content.lower() in ['シューター', 'ブラスター', 'リールガン', 'マニューバー', 'ローラー', 'フデ', 'チャージャー', 'スロッシャー', 'スピナー', 'シェルター']:
            type_name = message.content.lower()
            json_open = open('data/weapon.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            filtered_data = list(filter(lambda x: x["type"]["name"]["ja_JP"] == type_name, json_data))
            if filtered_data:
                buki = random.choice(filtered_data)
                ja_name = buki["name"]["ja_JP"]
                en_name = buki["name"]["en_US"]
                path = "images/main/" + buki["name"]["ja_JP"] + ".png"
                user = message.author.display_name
                await message.channel.send(f"{user}さんにおすすめの{type_name}は{ja_name}({en_name})！" , file=discord.File(path))

        cmd = message.content.split(" ")
        if cmd[0] == "/buki" and cmd[1:2]: # cmd[2]が存在するかどうか
            type_name = cmd[1]
            json_open = open('data/weapon.json', 'r',encoding='utf-8')
            json_data = json.load(json_open)
            filtered_data = list(filter(lambda x: x["type"]["name"]["ja_JP"] == type_name, json_data))
            if filtered_data:
                buki = random.choice(filtered_data)
                ja_name = buki["name"]["ja_JP"]
                en_name = buki["name"]["en_US"]
                path = "images/main/" + buki["name"]["ja_JP"] + ".png"
                user = message.author.display_name
                await message.channel.send(f"{user}さんにおすすめの{type_name}は{ja_name}({en_name})！" , file=discord.File(path))


        if message.content.lower() in ['gachi', 'ガチ', 'がち', 'gachima', 'ガチマ', 'がちま', 'ガチマッチ', 'がちまっち']:
            key = "ガチマッチ"
            link = "gachi/schedule"
            msg = getStageInfo(link, key)
            await message.channel.send(msg)

        if message.content.lower() in ['league', 'riguma', 'リグマ', 'りぐま', 'リーグマッチ', 'りーぐまっち']:
            key = "リーグマッチ"
            link = "league/schedule"
            msg = getStageInfo(link, key)
            await message.channel.send(msg)

        if message.content.lower() in ['regular', 'レギュラー', 'れぎゅらー', 'レギュラーマッチ', 'れぎゅらーまっち', 'nawabari', 'ナワバリ', 'なわばり', 'ナワバリバトル', 'なわばりばとる']:
            key = "ナワバリバトル"
            link = "regular/schedule"
            msg = getStageInfo(link, key, showRule=False)
            await message.channel.send(msg)

        if message.content.lower() in ['salmon', 'samon', 'sa-mon', 'サーモン', 'さーもん', 'サーモンラン', 'さーもんらん', 'サモラン', 'さもらん', 'coop', 'コープ', 'こーぷ', 'サケ', 'さけ', 'シャケ', 'しゃけ', '鮭']:
            key = "サーモンラン"
            link = "coop/schedule"
            msg = getCoopInfo(link, key)
            await message.channel.send(msg)

def setup(bot):
    bot.add_cog(spl(bot))