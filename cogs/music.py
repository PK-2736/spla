# import os
# import asyncio

# import discord
# import youtube_dl
# from discord.ext import commands
# from youtube_search import YoutubeSearch

# print("musicの読み込み完了")

# ydl_opts = {
#     'format': 'worstaudio/worst',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }]}

# class Music(commands.Cog):
#     def __init__(self, bot: discord.Client):
#         self.bot = bot
#         self.easy_embed = self.bot.easy_embed

#     guild_ids = [981474117020712970]  

#     music = discord.SlashCommandGroup("music", "音楽関連", guild_ids = guild_ids)

#     @music.command(name='play')
#     async def play(self, ctx: discord.ext.commands.Context, *args):
#         player = Player.get_or_start_player(ctx, self.easy_embed)
#         await player.add_song(' '.join(args))
#         await player.play()

#     @music.command(name='playlist')
#     async def play_list(self, ctx: discord.ext.commands.Context):
#         await Player.get_or_start_player(ctx, self.easy_embed).print_playlist()

#     @music.command(name='skip')
#     async def skip(self, ctx: discord.ext.commands.Context):
#         await Player.get_or_start_player(ctx, self.easy_embed).skip()

#     @music.command(name='pause')
#     async def pause(self, ctx: discord.ext.commands.Context):
#         await Player.get_or_start_player(ctx, self.easy_embed).pause()

#     @music.command(name='resume')
#     async def resume(self, ctx: discord.ext.commands.Context):
#         await Player.get_or_start_player(ctx, self.easy_embed).resume()

#     @music.command(name='clear')
#     async def stop(self, ctx: discord.ext.commands.Context):
#         await Player.get_or_start_player(ctx, self.easy_embed).clear()


# def setup(bot):
#     bot.add_cog(Music(bot))


# class Song():
#     def __init__(self, keyword, ctx):
#         self.infodict = YoutubeSearch(keyword, max_results=1).to_dict()
#         print(self.infodict)
#         if len(self.infodict) > 0:
#             self.infodict = self.infodict[0]
#             self.valid = True
#         else:
#             self.valid = False

#     def get_full_url(self):
#         return "https://youtube.com/" + self.infodict['url_suffix']

#     def get_short_title(self):
#         short_title = self.infodict['title'][:45] + "..." if len(self.infodict['title']) > 50 else self.infodict[
#             'title']
#         return short_title

#     def get_image_url(self):
#         return self.infodict['thumbnails'][0]


# class Player():
#     players = []

#     def __init__(self, ctx, easy_embed):
#         self.ctx = ctx
#         Player.players.append(self)
#         self.guild_id = ctx.guild.id
#         self.playlist = []
#         self.playing = False
#         self.easy_embed = easy_embed
#         self.channel = ctx.message.author.voice.channel

#     @staticmethod
#     def get_or_start_player(ctx, easy_embed):
#         for i in Player.players:
#             if i.guild_id == ctx.guild.id:
#                 i.ctx = ctx
#                 if not i.channel:
#                     i.channel = ctx.message.author.voice.channel
#                 return i
#         else:
#             return Player(ctx, easy_embed)

#     async def play(self):
#         if not self.playing:
#             self.playing = True
#             await self.play_next_song()
#             print("test")

#     async def resume(self):
#         if not self.playing:
#             self.playing = True
#             self.ctx.voice_client.resume()
#             await self.easy_embed.simple_message("Playlist resumed", self.ctx)

#     async def pause(self):
#         if self.playing:
#             self.playing = False
#             self.ctx.voice_client.pause()
#             await self.easy_embed.simple_message("Playlist paused", self.ctx)

#     def stop(self):
#         self.playing = False
#         self.ctx.voice_client.stop()

#     async def clear(self):
#         self.stop()
#         self.playlist = []
#         await self.easy_embed.simple_message("Playlist cleared", self.ctx)

#     async def add_song(self, keyword):
#         song = Song(keyword, self.ctx)
#         print(song)
#         if song.valid:
#             self.playlist.append(song)
#             await self.easy_embed.simple_message("Added: " + song.get_short_title(), self.ctx)
#         else:
#             await self.easy_embed.simple_message("Song not found", self.ctx)

#     async def play_next_song(self):
#         playlist = self.playlist
#         ctx = self.ctx
#         if len(playlist) > 0:
#             await self.easy_embed.simple_message("Playing: " + playlist[0].get_short_title(), self.ctx,
#                                                  image_url=playlist[0].get_image_url())
#             song = playlist[0].get_full_url()

#             if ctx.voice_client is None:
#                 vc = await self.channel.connect()

#             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                 info = ydl.extract_info(song, download=False)
#                 URL = info['formats'][0]['url']

#             playlist.pop(0)

#             ctx.voice_client.play(discord.FFmpegPCMAudio(URL))
#             ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source, 1)
#             while ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
#                 await asyncio.sleep(0.1)
#             await self.play_next_song()

#         else:
#             if ctx.voice_client:
#                 await ctx.voice_client.disconnect()
#             self.playing = False

#     async def print_playlist(self):
#         ctx = self.ctx
#         playlist = self.playlist
#         if len(playlist) > 0:
#             embed = discord.Embed(title="Current playlist: ", colour=0x7289da)
#             songlist = ""
#             for i in playlist:
#                 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                     video_title = i.get_short_title()
#                     songlist += "- " + video_title + "\n"
#             embed.add_field(name="Songs: ", value=songlist, inline=False)
#             await ctx.send(embed=embed)
#         else:
#             await self.easy_embed.simple_message("No songs in playlist!", self.ctx)

#     async def skip(self):
#         if self.ctx.voice_client:
#             self.ctx.voice_client.stop()
#             await self.easy_embed.simple_message("Song skipped!", self.ctx) 