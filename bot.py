import json
import asyncio

import discord
from discord.ext import commands    # gets the bot commands archive
from discord.utils import get       # gets the finding functions
from discord.ext import commands
from Engine import Engine
from img import draw_board
import helper
import game


CONFIG = json.load(open("./config.json"))

TOKEN = CONFIG["token"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(pass_context=True)
async def generate(ctx, *, FEN):
    e = Engine(FEN)
    e.load_board_from_fen()
    draw_board(e)
    file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
    await ctx.send(file=file_)

@bot.command(pass_context=True)
async def challenge(ctx, user='', *, FEN=''):
    if not user:
        await ctx.send("Please select a user to challenge!")
    else:
        id = int(user[2:-1])
        # if ctx.author.id == id:
        #     await ctx.send("You cannot challenge yourself!")
        #     return

        msg = await ctx.send(f"{user}: Please accept or deny this challenge.")
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")

        def check(reaction, user):
            return user.id == id and reaction.message.id == msg.id
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if reaction.emoji == "✅":
                await ctx.send("Accepted!")
                if not FEN:
                    FEN = CONFIG["baseFEN"]
                await game.run(bot, ctx, FEN, id)
            elif reaction.emoji == "❌":
                await ctx.send("Denied!")

        except asyncio.TimeoutError:
            await ctx.send("Challenge has timed out.")

@bot.command(pass_context=True)
async def code(ctx):
    await ctx.send("My code can be found here:\nhttps://github.com/ryankarch/chessbot")

@bot.command(pass_context=True)
async def moves(ctx, move, *, FEN):
    e = Engine(FEN)
    e.switch_player()
    try:
        move = helper.get_cell_tuple(move)
        e.advance_turn()
        moves = e.board_piece[move[0]][move[1]].return_moves()
    except:
        moves = []
    draw_board(e, moves)
    file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
    await ctx.send(file=file_)
        

bot.run(TOKEN)