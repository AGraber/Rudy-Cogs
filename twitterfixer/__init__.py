from .twittrerfixer import TwitterFixer


async def setup(bot):
    await bot.add_cog(TwitterFixer(bot))
