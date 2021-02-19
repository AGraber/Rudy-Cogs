import discord
import time
import random
from string import ascii_lowercase
from redbot.core import commands

gaslinks = [
    'https://i.imgur.com/iuuFvBb.jpg',
    'https://cdn.discordapp.com/attachments/477293251737550861/577684575388565541/tWzddexCr7NKfzYKafUY33wUuzYw56GvwVsOiEyrGMQ.png',
    'https://cdn.discordapp.com/attachments/639337212424617994/645094552222433280/tumblr_nw2t03DKNH1ufq0ayo1_1280.png',
    'https://cdn.discordapp.com/attachments/639337212424617994/645095656930934784/itsuki-takumi-iketani-at-gas-station-initial-d.png'
]

# rcrp guild ID
rcrpguildid = 93142223473905664

# roles
adminrole = 293441894585729024
managementrole = 310927289317588992
ownerrole = 293303836125298690
staffroles = [ownerrole, adminrole, managementrole]

# the age of rudy. used for the fancy time delta in the age command
rudyage = 1409529600

# lol this is so ghetto
path = __file__
path = path.replace('rudyfun.py', '')


async def admin_check(ctx: commands.Context):
    if ctx.guild is not None and ctx.guild.id == rcrpguildid:
        for role in ctx.author.roles:
            if role.id in staffroles:
                return True
        return False
    else:
        return True


def pretty_time_delta(seconds: int):
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(seconds)
    years, seconds = divmod(seconds, 31556952)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if years > 0:
        return '%s%dy %dd %dh %dm %ds' % (sign_string, years, days, hours, minutes, seconds)
    elif days > 0:
        return '%s%dd %dh %dm %ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s%dh %dm %ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s%dm %ds' % (sign_string, minutes, seconds)
    else:
        return '%s%ds' % (sign_string, seconds)


class FunCommands(commands.Cog):
    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def give(self, ctx: commands.Context, item: str = None):
        """Gives Rudy a number of different items which he may or may not enjoy"""
        if item == 'poptart':
            await ctx.send("* Rudy enjoys the poptart but vomits it back up about twenty minutes later. * (this actually happened i fucking hate my sister)")
        elif item == 'treat':
            await ctx.send("* Rudy takes the treat from your hand and runs off into another room with it, more than likely a room that has carpet. He chews on the treat clumsily, creating a mess of crumbs on the floor. He eventually sniffs out the crumbs he failed to ingest and finishes off every last one. *")
        elif item == 'bone':
            await ctx.send("* Rudy happily takes the bone from you and runs off with it, however he neglects to actually chew on said bone. He instead leaves the bone in an accessible location at all times and waits for moments of opportune happiness or excitement (e.g, someone returning home) to put it back in his mouth. Once peak excitement levels are reached, he prances around the house with the bone in his mouth, doing multiple laps around the kitchen with it as well. *")
        else:
            await ctx.send("*Rudy stares at your empty hand disappointed. *")

    @commands.command()
    @commands.guild_only()
    @commands.check(admin_check)
    async def emojisay(self, ctx: commands.Context, *, message: str):
        """Converts your garbage text into a message made entirely of emojis"""
        message = message.lower()
        newmessage = []
        for c in message:
            if c in ascii_lowercase:
                newmessage.append(':regional_indicator_{0}:'.format(c))
            else:
                newmessage.append(c)

        newmessage = ''.join(newmessage)
        await ctx.message.delete()

        if len(newmessage) >= 2000:
            await ctx.send("Final message was too long.")
        else:
            await ctx.send(newmessage)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def gasgasgas(self, ctx: commands.Context):
        """Got any anime gas?"""
        await ctx.send(random.choice(gaslinks))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def dozed(self, ctx: commands.Context):
        """nigga dozed off real quick"""
        await ctx.send(file=discord.File(f'{path}/files/dozed.mp3'))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def cunt(self, ctx: commands.Context):
        """unforgiveable"""
        await ctx.send(file=discord.File(f'{path}/files/cunt.mp3'))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def wheels(self, ctx: commands.Context):
        """a tragic tale"""
        await ctx.send("Never put wheels on your PC", file=discord.File(f'{path}/files/wheels.mp3'))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def valero(self, ctx: commands.Context):
        """Hey guys, Valero here"""
        await ctx.send(file=discord.File(f'{path}/files/valero.mp3'))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 60)
    async def bazinga(self, ctx: commands.Context):
        """Bazinga!"""
        await ctx.send(file=discord.File(f'{path}/files/bazinga.mp3'))

    @commands.command()
    @commands.guild_only()
    async def ygay(self, ctx: commands.Context, target: discord.Member):
        """Ask why someone is in fact gay"""
        await ctx.message.delete()
        await ctx.send(f'{target.mention}, why are you gay?', file=discord.File(f'{path}/files/why-are-you-gay.mp3'))

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def pet(self, ctx: commands.Context, *, location: str = None):
        """Gives Rudy some pets"""
        if location == 'head' or location == 'ears':
            await ctx.send("* You pet Rudy's head, specifically behind the ears. He enjoys this very much and sticks his nose out directly towards you as a reaction to the affection. *")
        elif location == 'lower back':
            await ctx.send("* You give Rudy a nice petting on his lower back, maybe sneaking in some back scratches too. He enjoys this very much and pokes his nose into the air as a reaction to the affection. *")
        else:
            await ctx.send("*You pet Rudy. He thinks it's pretty neat. *")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def age(self, ctx: commands.Context):
        """Displays the age of Rudy"""
        rudy_age = pretty_time_delta(int(time.time()) - rudyage)
        await ctx.send(f"Rudy's age: {rudy_age}")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def makerudyfat(self, ctx: commands.Context):
        """Delivers a kind response to those who want Rudy to be a chunky dog"""
        await ctx.send("Rudy can't be fat you fucking subhuman piece of shit.")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def bellyrub(self, ctx: commands.Context):
        """Gives Rudy a much-desired bellyrub"""
        await ctx.send("* You give Rudy a bellyrub. He kicks at your hand like a fucking idiot. *")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def walk(self, ctx: commands.Context):
        """Take Rudy on a walk!"""
        await ctx.send("* Upon hearing news of a potential walk, Rudy fucking loses his shit and starts to jump at you like a madman. He pants heavily while jumping at you repeatedly until you hopefully grab his leash and take him on a nice walk through the nearby park. *")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def weight(self, ctx: commands.Context):
        """Sends Rudy's weight"""
        await ctx.send("I weigh 12 pounds. (5.44 KG or 0.85 stone for foreign people)")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def sit(self, ctx: commands.Context):
        """Orders Rudy to sit"""
        await ctx.send("* Rudy obediently sits down like a good boy. His tail wags back and forth a few times as well. *")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def stay(self, ctx: commands.Context):
        """Orders Rudy to stay"""
        await ctx.send("* Rudy sits down at his current position with one ear straight up and the other floppy. He eventually gets dog brain syndrome and stands up, following you. *")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def brisket(self, ctx: commands.Context):
        """A terrible story from a terrible night"""
        await ctx.send("Once upon a time, I wad fed copious amounts of delicious brisket by a drunk man. I have a really sensitive stomach and I'm only supposed to eat special dog food which helps relax it. During the middle of the night when I was asleep, I felt a pain in my stomach and started to cough and gag a bunch. My owner woke up due to the sounds and quickly rushed me into the kitchen in hopes to take me outside. I then proceeded to projectile vomit on the floor several times, it was not a fun experience. My poor owner had to clean up the mess I created. I haven't been fed table food since.")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def rabbits(self, ctx: commands.Context):
        """A terrible story about some rabbits"""
        await ctx.send("Once upon a time, there was a rabbit that kept intruding in the back yard every once in a while. Every time I noticed it, I would sprint off towards it for reasons my dog brain can't explain. One day I was sniffing around the yard and noticed a bunch of little baby rabbits in a hole dug in MY YARD. My instinctive dog reaction was to murder every single little rabbit that I could find. I even ripped two of them in half with my dog teeth.")

    @commands.command()
    @commands.cooldown(1, 60)
    @commands.guild_only()
    async def bathe(self, ctx: commands.Context):
        """Give Rudy a bath!"""
        await ctx.send("* You give Rudy a bath. He dislikes it heavily. *")

    @commands.command()
    @commands.guild_only()
    async def unixtimestamp(self, ctx: commands.Context):
        """Sends the unix timestamp for Melvin (It's not -1)"""
        value = int(time.time())
        await ctx.send(f"CURRENT UNIX TIMESTAMP VALUE: {value}")

    @commands.command()
    @commands.guild_only()
    async def bruh(self, ctx: commands.Context):
        """Bruh"""
        await ctx.send("https://i.imgur.com/7QWYKgO.jpg")
