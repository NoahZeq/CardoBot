import datetime
import nextcord, asyncio

from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        channel_name = ctx.channel.name
        logs_channel = self.bot.get_channel(969097826036490290)
        
        await ctx.message.delete()
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=limit)
        
        purge_embed = nextcord.Embed(
            title='Purge [;purge]',
            description=f"Successfully purged {limit} messages in #{channel_name}. \n Command executed by {ctx.author}.",
            color=nextcord.Color.blue()
        )
        purge_embed.set_footer(text=str(datetime.datetime.now()))
        await logs_channel.send(embed=purge_embed)
        
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        role = nextcord.utils.get(member.guild.roles, id=969095291796090880)
        channel = self.bot.get_channel(969094521612824597)
        welcome_embed = nextcord.Embed(
            description=f'**Welcome to GGCPH!** {member.mention} \n \n <#969115039564980234> \n <#969147216147152936>',
            color=nextcord.Color.yellow()
        )
        
        await member.add_roles(role)
        await channel.send(embed=welcome_embed)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        def is_me(m):
                return m.author == self.bot.user
        channel1 = self.bot.get_channel(969233174834057316)
        channel2 = 969094521612824605
        channel3 = 969094521956761650
        if message.channel.id != channel1.id and message.channel.id != channel2 and message.channel.id != channel3:
            return
        if message.author.bot:
            return
        elif not message.attachments:
            await message.delete()  
        elif (message.channel.id == 969233174834057316):
            await message.add_reaction("🔼")
            await message.add_reaction("🔽")
            
            await channel1.purge(limit=2, check=is_me)
            messagebot = await channel1.send("__**Reminder!**__ \n \nThis channel only accepts messages that has an attachment.")  
        
        channel = self.bot.get_channel(969094521612824605)
        if message.channel.id != channel.id:
            return
        if message.author.bot:
            return
        elif (message.channel.id == 969094521612824605):
            await message.add_reaction("🔼")
            await message.add_reaction("🔽")
            
            await channel.purge(limit=2, check=is_me)
            messagebot = await channel.send("__**Reminder!**__ \n \nThis channel only accepts messages that has an attachment.")
        elif not message.attachments:
            await message.delete()
        
        channel = self.bot.get_channel(969094521956761650)
        if message.author.bot:
            return
        elif (message.channel.id == 969094521956761650):
            await message.add_reaction("🔼")
            await message.add_reaction("🔽")
            
            await channel.purge(limit=2, check=is_me)
            messagebot = await channel.send("__**Reminder!**__ \n \nThis channel only accepts messages that has an attachment.")
        elif not message.attachments:
            await message.delete()
    
def setup(bot):
    bot.add_cog(Moderation(bot))