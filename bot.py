import json

import discord
from discord.ext import commands    # gets the bot commands archive
from discord.utils import get       # gets the finding functions
from discord.ext import commands

CONFIG = json.load(open("./config.json"))

TOKEN = CONFIG["token"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)



bot.run(TOKEN)