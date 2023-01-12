import json

import discord
from discord.ext import commands    # gets the bot commands archive
from discord.utils import get       # gets the finding functions
from discord.ext import commands
from game import Board
from img import draw_board


CONFIG = json.load(open("./config.json"))

TOKEN = CONFIG["token"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(pass_context=True)
async def generate(ctx, *, FEN):
    b = Board(FEN)
    b.parse_fen()
    draw_board(b.board)
    file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
    await ctx.send(file=file_)

bot.run(TOKEN)