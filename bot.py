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
    # embed_ = discord.Embed(title = "Board", color = 0xF1C40F)
    # file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
    # embed_.set_image(url="attachment://board.jpg")
    # await ctx.send(file=file_, embed=embed_)

bot.run(TOKEN)