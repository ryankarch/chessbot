import discord
from discord.ext import commands    # gets the bot commands archive
import asyncio

import random
from board import Board
import img
import helper


async def run(bot: commands.Bot, ctx: commands.Context, FEN: str, id):
    b = Board(FEN)
    if random.randint(0, 1) == 0:
        b.white.setid(ctx.author.id)
        b.black.setid(id)
    else:
        b.white.setid(id)
        b.black.setid(ctx.author.id)
    b.load_board_from_fen()
    turn = 0
    current_id = b.white.id
    moves = []
    while True:
        if turn:
            def check(message):
                if current_id == message.author.id:
                    try:
                        helper.get_cell_tuple(message.content)
                        return True
                    except:
                        return True if message.content == "resign" else False
            try:
                message = await bot.wait_for('message', timeout=600.0, check=check)
                if message.content == "resign":
                    await ctx.send(f"<@{current_id}> has resigned!")
                    return
                else:
                    move = helper.get_cell_tuple(message.content)
                    moves = b.board_piece[move[0]][move[1]].get_moves(b.board_piece)
            except asyncio.TimeoutError:
                await ctx.send("Game has timed out.")
                return
        img.draw_board(b, moves)
        file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
        await ctx.send(f"<@{b.white.id}>, it's your turn!", file=file_)
        b.switch_player()
        turn += 1
        current_id = b.black.id