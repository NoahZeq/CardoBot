import nextcord

from nextcord.ext import commands

class Reactionrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    """@commands.Cog.listener()
    async def on_ready(self):
        Channel = self.bot.get_channel(969147216147152936)
        Text = nextcord.Embed(
            title='**¤ STATUS**',
            description="👤・<@&969207174653968424>\n💑・<@&969207321152598026>\n💌・<@&969207364882419752>\n❔・<@&969207472411783208>",
            color=nextcord.Color.blue()
        )
        Text.set_image(url='https://cdn.discordapp.com/attachments/969150834397048842/969206764060962897/Add_a_heading_6.png')
        Moji = await Channel.send(embed=Text)
        await Moji.add_reaction('👤')
        await Moji.add_reaction('💑')
        await Moji.add_reaction('💌')
        await Moji.add_reaction('❔')"""
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id) # Get guild
        member = nextcord.utils.get(guild.members, id=payload.user_id) # Get the member out of the guild
        # The channel ID should be an integer:
        if payload.channel_id == 969147216147152936: # Only channel where it will work
            if str(payload.emoji) == "👨": # Your emoji
                role = nextcord.utils.get(payload.member.guild.roles, id=969151902719827988)
            elif str(payload.emoji) == "👩": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969151983409827891)
            elif str(payload.emoji) == "🌈": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969152139811229747)
            elif str(payload.emoji) == "🟢": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157451624644609)
            elif str(payload.emoji) == "🔵": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157560282275850)
            elif str(payload.emoji) == "🔴": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157621535875084)
            elif str(payload.emoji) == "<:valorant:969160808376463360>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159372146085918)
            elif str(payload.emoji) == "<:codm:969168251420565534>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159443860324372)
            elif str(payload.emoji) == "<:roblox:969168349999288320>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159832038944768)
            elif str(payload.emoji) == "<:minecraft:969168717386772510>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159976075526154)
            elif str(payload.emoji) == "<:mobilelegends:969169203858923551>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969160031561990154)
            elif str(payload.emoji) == "<:genshinimpact:969169535326375956>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969160157944762368)
            elif str(payload.emoji) == "👤": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207174653968424)
            elif str(payload.emoji) == "💑": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207321152598026)
            elif str(payload.emoji) == "💌": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207364882419752)
            elif str(payload.emoji) == "❔": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207472411783208)
            else:
                role = nextcord.utils.get(guild.roles, name=payload.emoji)
            if role is not None: # If role exists
                await payload.member.add_roles(role)
                
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild = self.bot.get_guild(payload.guild_id) # Get guild
        member = nextcord.utils.get(guild.members, id=payload.user_id) # Get the member out of the guild
        # The channel ID should be an integer:
        if payload.channel_id == 969147216147152936: # Only channel where it will work
            if str(payload.emoji) == "👨": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969151902719827988)
            elif str(payload.emoji) == "👩": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969151983409827891)
            elif str(payload.emoji) == "🌈": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969152139811229747)
            elif str(payload.emoji) == "🟢": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157451624644609)
            elif str(payload.emoji) == "🔵": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157560282275850)
            elif str(payload.emoji) == "🔴": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969157621535875084)
            elif str(payload.emoji) == "<:valorant:969160808376463360>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159372146085918)
            elif str(payload.emoji) == "<:codm:969168251420565534>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159443860324372)
            elif str(payload.emoji) == "<:roblox:969168349999288320>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159832038944768)
            elif str(payload.emoji) == "<:minecraft:969168717386772510>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969159976075526154)
            elif str(payload.emoji) == "<:mobilelegends:969169203858923551>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969160031561990154)
            elif str(payload.emoji) == "<:genshinimpact:969169535326375956>": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969160157944762368)
            elif str(payload.emoji) == "👤": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207174653968424)
            elif str(payload.emoji) == "💑": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207321152598026)
            elif str(payload.emoji) == "💌": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207364882419752)
            elif str(payload.emoji) == "❔": # Your emoji
                role = nextcord.utils.get(member.guild.roles, id=969207472411783208)
            else:
                role = nextcord.utils.get(guild.roles, name=payload.emoji)
            if role is not None: # If role exists
                await member.remove_roles(role)
    
def setup(bot):
    bot.add_cog(Reactionrole(bot))