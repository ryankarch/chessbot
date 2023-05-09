import discord
from discord.ext import commands    # gets the bot commands archive
import asyncio

import random
from Engine import Engine
import img
import helper


async def run(bot: commands.Bot, ctx: commands.Context, FEN: str, id):
    e = Engine(FEN)
    if random.randint(0, 1) == 0:
        e.white.setid(ctx.author.id)
        e.black.setid(id)
    else:
        e.white.setid(id)
        e.black.setid(ctx.author.id)
    turn = 0
    current_id = e.white.id
    moves = []
    e.switch_player()
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
                    try:
                        move = helper.process_move(message.content, e)
                    except:
                        await ctx.send("Invalid move, please try again.")
                        continue
                    if not move:
                        await ctx.send("Invalid move, please try again.")
                        continue
                    else:
                        e.move(move)
            except asyncio.TimeoutError:
                await ctx.send("Game has timed out.")
                return
        result = e.advance_turn()
        e.update_check(result)
        turn += 1
        current_id = e.white.id if e.rules["move"] == 'w' else e.black.id
        img.draw_board(e, moves)
        file_ = discord.File("./assets/RunningBoard.jpg", filename="board.png")
        if result == '#':
            winner = e.black.id if e.rules["move"] == 'w' else e.white.id
            await ctx.send(f"<@{winner}> has won!", file=file_)
            return
        else:
            await ctx.send(f"<@{current_id}>, it's your turn!", file=file_)