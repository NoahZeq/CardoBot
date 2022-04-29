import nextcord, bot_token
import os

from nextcord.ext import commands

os.chdir('E:/Dev/Py/CardoBot')

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print('Bot Online!')
    
for filename in os.listdir("./cogs"):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')
        
client = nextcord.Client(intents=intents)
bot.run(bot_token.TOKEN)