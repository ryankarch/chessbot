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
    turn = 0
    current_id = b.white.id
    moves = []
    b.switch_player()
    while True:
        if turn:
            def check(message):
                if current_id == message.author.id:
                    return helper.check_valid(message.content)
            try:
                message = await bot.wait_for('message', timeout=600.0, check=check)
                if message.content == "resign":
                    await ctx.send(f"<@{current_id}> has resigned!")
                    return
                else:
                    move = helper.process_move(message.content, b)
                    if not move:
                        await ctx.send("Invalid move, please try again.")
                        continue
                    else:
                        b.move(move)
            except asyncio.TimeoutError:
                await ctx.send("Game has timed out.")
                return
        result = b.advance_turn()
        b.update_check(result)
        turn += 1
        current_id = b.white.id if b.rules["move"] == 'w' else b.black.id
        img.draw_board(b, moves)
        file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
        await ctx.send(f"<@{b.white.id}>, it's your turn!", file=file_)