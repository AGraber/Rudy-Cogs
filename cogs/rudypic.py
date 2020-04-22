import discord
import random
from imgurpython import ImgurClient
from discord.ext import commands
from cogs.utility import rudyfriend, rcrpguildid

#imgur client handler
imclient = ImgurClient('6f85cfd1f822e7b', '629f840ae2bf44b669560b64403c3f8511293777')

async def isrudyfriend(ctx):
    if ctx.guild.id == rcrpguildid:
        if rudyfriend in [role.id for role in ctx.author.roles]:
            return True
        else:
            return False
    else:
        return True

async def SendRandomAlbumPicture(ctx, album):
    pictures = []
    for image in imclient.get_album_images(album):
        pictures.append(image.link)
    await ctx.send(random.choice(pictures))

class RudypicCog(commands.Cog, name="rudypic"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Sends an adorable picture of Rudy")
    @commands.guild_only()
    @commands.check(isrudyfriend)
    async def rudypic(self, ctx):
        await SendRandomAlbumPicture(ctx, 'WLQku0l')

    @commands.command(help = "Sends an adorable picture of Sammy")
    @commands.guild_only()
    @commands.check(isrudyfriend)
    async def sammypic(self, ctx):
        await SendRandomAlbumPicture(ctx, 'VfKwj4H')

    @commands.command(help = "Sends an adorable picture of Milo")
    @commands.guild_only()
    @commands.check(isrudyfriend)
    async def milopic(self, ctx):
        await SendRandomAlbumPicture(ctx, 'h3VORpQ')

    @commands.command(help = "Sends a legendary gizmo quote.")
    @commands.is_owner()
    async def gizmo(self, ctx):
        await SendRandomAlbumPicture(ctx, 'SlgjJJu')
    

def setup(bot):
    bot.add_cog(RudypicCog(bot))