import asyncio
import os
import random
import json
import requests
import discord
from discord.ext import commands
from discord import Embed, AllowedMentions
from discord.commands import slash_command, Option

print("splassの読み込み完了")

class Game(commands.Cog):
    """トレーニングといったお遊び系のコマンドがあるカテゴリーです"""
    def __init__(self, bot):
        self.bot = bot
        self.stage_info = None
        self.s_endpoint = 'https://stat.ink/api/v2'
        self.spla_api_key = os.getenv('SPLATOON2_KEY')

    guild_ids = [981474117020712970]  

    spla = discord.SlashCommandGroup("spla", "フレンドコード関連", guild_ids = guild_ids)

    @spla.command(description='Splatoon2のステージ情報を取得します',
                      usage='[対戦ルールタイプ] <n(次の時間帯)>')
    async def stage2(self, ctx, s_type: Option(str, "r(レギュラー) l(リーマッチ) s(サーモンラン) g(ガチマッチ)"), s_next=None):
        def get_stage(game, time_next: bool):
            if game == 'regular':
                if time_next:
                    res = requests.get('https://spla2.yuu26.com/regular/next')
                    return res.json()['result'][0]
                else:
                    res = requests.get('https://spla2.yuu26.com/regular/now')
                    return res.json()['result'][0]
            elif game == 'gachi':
                if time_next:
                    res = requests.get('https://spla2.yuu26.com/gachi/next')
                    return res.json()['result'][0]
                else:
                    res = requests.get('https://spla2.yuu26.com/gachi/now')
                    return res.json()['result'][0]
            elif game == 'league':
                if time_next:
                    res = requests.get('https://spla2.yuu26.com/league/next')
                    return res.json()['result'][0]
                else:
                    res = requests.get('https://spla2.yuu26.com/league/now')
                    return res.json()['result'][0]
            elif game == 'coop':
                if time_next:
                    res = requests.get('https://spla2.yuu26.com/coop/schedule')
                    return res.json()['result'][1]
                else:
                    res = requests.get('https://spla2.yuu26.com/coop/schedule')
                    return res.json()['result'][0]

        if s_type is None:
            no_type_msg = Embed(description='ステージ情報のタイプ(r, g, l, s)を指定してください\n'
                                            'r: レギュラーマッチ\ng: ガチマッチ\nl: リーグマッチ\ns: サーモンラン')
            await ctx.respond(embed=no_type_msg, allowed_mentions=AllowedMentions.none())
        elif s_type == 'r':
            if s_next is None:
                self.stager_info = get_stage('regular', False)
            elif s_next == 'n':
                self.stager_info = get_stage('regular', True)

            stage_info = self.stager_info
            rule_name = stage_info["rule"]
            stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
            s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
            e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
            image_url = random.choice([stage_info['maps_ex'][0]['image']])
            image_url2 = random.choice([stage_info['maps_ex'][1]['image']])

            de_msg = f'**ルール**\n\n{rule_name}\n**ステージ**\n\n{stage}\n\n' \
                     f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
            embed = Embed(title='Splatoon2 ステージ情報 | レギュラーマッチ',
                          description=de_msg,
                          color=261888)  # カラー:ライトグリーン)
            embed.set_image(url=image_url)
            embed.set_thumbnail(url=image_url2)
            await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

        elif s_type == 'g':
            if s_next is None:
                self.stage_info = get_stage('gachi', False)
            elif s_next == 'n':
                self.stage_info = get_stage('gachi', True)

            stage_info = self.stage_info
            rule_name = stage_info["rule"]
            stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
            s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
            e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
            image_url = random.choice([stage_info['maps_ex'][0]['image']])
            image_url2 = random.choice([stage_info['maps_ex'][1]['image']])

            de_msg = f'**ルール**\n\n{rule_name}\n\n**ステージ**\n\n{stage}\n\n' \
                     f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
            embed = Embed(title='Splatoon2 ステージ情報 | ガチマッチ',
                          description=de_msg,
                          color=14840346)  # カラー:オレンジ
            embed.set_image(url=image_url)
            embed.set_thumbnail(url=image_url2)
            await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

        elif s_type == 'l':
            if s_next is None:
                self.stage_info = get_stage('league', False)
            elif s_next == 'n':
                self.stage_info = get_stage('league', True)

            stage_info = self.stage_info
            rule_name = stage_info["rule"]
            stage = f'・{stage_info["maps"][0]}\n・{stage_info["maps"][1]}'
            s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
            e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
            image_url = random.choice([stage_info['maps_ex'][0]['image']])
            image_url2 = random.choice([stage_info['maps_ex'][1]['image']])


            de_msg = f'**ルール**\n\n{rule_name}\n\n**ステージ**\n\n{stage}\n\n' \
                     f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
            embed = Embed(title='Splatoon2 ステージ情報 | リーグマッチ',
                          description=de_msg,
                          color=15409787)  # カラー:ピンク
            embed.set_image(url=image_url)
            embed.set_thumbnail(url=image_url2)
            await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

        elif s_type == 's':
            if s_next is None:
                self.stage_info = get_stage('coop', False)
            elif s_next == 'n':
                self.stage_info = get_stage('coop', True)

            stage_info = self.stage_info
            stage = stage_info["stage"]["name"]
            image_url = stage_info['stage']['image']
            s_t = str(stage_info['start']).replace('-', '/', 2).replace('T', ' | ')
            e_t = str(stage_info['end']).replace('-', '/', 2).replace('T', ' | ')
            weapons = ''
            for we in stage_info['weapons']:
                weapons += f'・{we["name"]}\n'

            de_msg = f'**ステージ**\n\n{stage}\n\n**支給ブキ**\n\n{weapons}\n' \
                     f'**時間帯**\n\nSTART: {s_t}\nEND: {e_t}\n'
            embed = Embed(title='Splatoon2 ステージ情報 | サーモンラン',
                          description=de_msg,
                          color=15442812)  # カラー:薄橙
            embed.set_image(url=image_url)
            await ctx.respond(embed=embed, allowed_mentions=AllowedMentions.none())

    @spla.command(description='Splatoon2のいろんな情報を取得します',
                    usage='[取得キー] <find/f> <su=名前/sp=名前>',
                    aliases=['splainfo', 'sp-info', 'spinfo'],
                    brief=['【取得キーリスト】we: ブキ\n'
                           '【絞り込み検索】su=名前: サブウェポン, sp=名前: スペシャル\n'
                           '【実行例】\n'
                           '・ブキリスト: {cmd}spinfo we f sp=ナイスダマ\n'
                           '・ブキリスト: {cmd}spinfo we f su=クイックボム']
                    )
    async def spla_info(self, ctx):
        if ctx.invoked_subcommand is None:
            return

    @spla.command(description='Splatoon2のいろんな情報を取得します')
    async def we(self, ctx, search=None, name=None):
        endpoint = f'{self.s_endpoint}/weapon'
        num_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        if search is None:
            response = requests.get(endpoint)
            status = response.status_code
            res_data = response.json()
            if status != 200:
                print(res_data)
            else:
                des_msg = []
                we_list = {'shooter': 'シューター', 'blaster': 'ブラスター', 'reelgun': 'リールガン', 'maneuver': 'マニューバー',
                           'roller': 'ローラー', 'brush': 'フデ', 'charger': 'チャージャー', 'slosher': 'スロッシャー',
                           'splatling': 'スピナー', 'brella': 'シェルター'}
                for num in range(len(we_list)):
                    des_msg.append(f'{num_list[num]} : {we_list[list(we_list)[int(num)]]}')
                msg_embed = Embed(title='武器リスト',
                                  description='武器の種類を選んでください\n\n{}'.format('\n'.join(des_msg)))

                def check(reaction, user):
                    return user == ctx.author and (str(reaction.emoji) in num_list or str(reaction.emoji) == '⏹') \
                           and reaction.message.channel == ctx.channel

                def check_2(reaction, user):
                    return user == ctx.author and (str(reaction.emoji) == '◀' or str(reaction.emoji) == '⏹') \
                           and reaction.message.channel == ctx.channel

                def get_weapon(emoji):
                    e_n = num_list.index(emoji)
                    weapon_type = list(we_list)[e_n]
                    weapon_list = []
                    for data in res_data:
                        if data['type']['key'] == weapon_type:
                            w_name = data['name']['ja_JP']
                            w_sp = data['special']['name']['ja_JP']
                            weapon_list.append(f'・{w_name} ({w_sp})')
                    return weapon_list, we_list[list(we_list)[int(num)]]

                while_msg = True
                while while_msg:
                    msg = await ctx.respond(embed=msg_embed, allowed_mentions=AllowedMentions.none())
                    for num in range(len(we_list)):
                        await msg.add_reaction(num_list[num])
                    await msg.add_reaction('⏹')
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)
                    except asyncio.TimeoutError:
                        await msg.clear_reactions()
                        while_msg = False
                    else:
                        await msg.clear_reactions()
                        if str(reaction.emoji) == '⏹':
                            await msg.edit(embed=Embed(description='終了しました'))
                            while_msg = False
                        else:
                            we_r, we_t = get_weapon(str(reaction.emoji))
                            we_msg = Embed(title=f'{we_t} の一覧', description='\n{}\n'.format('\n'.join(we_r)))
                            await msg.edit(embed=we_msg)
                            await msg.add_reaction('◀')
                            await msg.add_reaction('⏹')
                            try:
                                reaction_2, user_2 = await self.bot.wait_for('reaction_add', timeout=60, check=check_2)
                            except asyncio.TimeoutError:
                                await msg.clear_reactions()
                                while_msg = False
                            else:
                                if str(reaction_2.emoji) == '◀':
                                    await msg.clear_reactions()
                                    await msg.delete()
                                    continue
                                elif str(reaction_2.emoji) == '⏹':
                                    await msg.clear_reactions()
                                    while_msg = False

        elif (search == 'find' and name is not None) or (search == 'f' and name is not None):
            if name.startswith('sp='):
                sp_name = name.replace('sp=', '')
                res = self.bot.splatoon.get_weapons('special', sp_name)
                if res is None:
                    await ctx.respond(embed=Embed(description='ブキが見つかりませんでした'), allowed_mentions=AllowedMentions.none())
                else:
                    re_embed = self.bot.splatoon.sort_weapons(sp_name, res)
                    await ctx.respond(embed=re_embed, allowed_mentions=AllowedMentions.none())
            elif name.startswith('su='):
                su_name = name.replace('su=', '')
                res = self.bot.splatoon.get_weapons('sub', su_name)
                if res is None:
                    await ctx.respond(embed=Embed(description='ブキが見つかりませんでした'), allowed_mentions=AllowedMentions.none())
                else:
                    re_embed = self.bot.splatoon.sort_weapons(su_name, res)
                    await ctx.respond(embed=re_embed, allowed_mentions=AllowedMentions.none())


    # @spla.command(description='サイコロを振ります')
    # async def dice(self, ctx):
    #     image = {
    #         'dice_1': 'https://cdn.discordapp.com/attachments/867004595079479296/867004682983047169/dice_1.jpg',
    #         'dice_2': 'https://cdn.discordapp.com/attachments/867004595079479296/867004694625648650/dice_2.jpg',
    #         'dice_3': 'https://cdn.discordapp.com/attachments/867004595079479296/867004690960482314/dice_3.jpg',
    #         'dice_4': 'https://cdn.discordapp.com/attachments/867004595079479296/867004690175492096/dice_4.jpg',
    #         'dice_5': 'https://cdn.discordapp.com/attachments/867004595079479296/867004688132997130/dice_5.jpg',
    #         'dice_6': 'https://cdn.discordapp.com/attachments/867004595079479296/867004685352042516/dice_6.jpg'
    #     }

    #     des_text = ['コロコロコロ...\n> **[dice]**', 'コロコロコロ...\n転がってゆく\n> **[dice]**',
    #                 'コロ..コロ..コロ..\nまだ転がる\n> **[dice]**']
    #     dice_embed = Embed(title='サイコロ')
    #     dice_embed.set_thumbnail(url=image['dice_1'])
    #     dice_msg = await ctx.respond(embed=dice_embed, allowed_mentions=AllowedMentions.none())
    #     await asyncio.sleep(2)
    #     for t in des_text:
    #         random_int = random.randint(1, 6)
    #         edit_embed = Embed(title='サイコロ',
    #                            description=t.replace('[dice]', f'{random_int}'))
    #         edit_embed.set_thumbnail(url=image[f'dice_{random_int}'])
    #         await dice_msg.edit(embed=edit_embed)
    #         await asyncio.sleep(1.5)

    #     random_int = random.randint(1, 6)
    #     edit_embed = Embed(title='サイコロ',
    #                        description=f'結果！！ \n> **{random_int}** が出ました！')
    #     edit_embed.set_thumbnail(url=image[f'dice_{random_int}'])
    #     await dice_msg.edit(embed=edit_embed)

def setup(bot):
    bot.add_cog(Game(bot))