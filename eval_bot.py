import asyncio
import inspect
import logging
import io
import sys
import traceback
import discord
import discord.ext.commands as commands

logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='#!')


bucket = {}
_ = None


@bot.command(name='aeval')
async def asyncdo(ctx, *, cmd):
    global bucket
    global _
    if cmd.endswith('!r'):
        cmd = cmd[:-2]
        meth = repr
    else:
        meth = str

    try:
        _ = await eval(cmd)
        await ctx.send(meth(_))
    except:
        pass


@bot.command(name='eval')
async def do(ctx, *, cmd):
    global bucket
    global _
    _ = eval(cmd)
    await ctx.send(_)


@bot.command(name='exec')
async def execute(ctx, *, cmd):
    global _
    global bucket

    old_stdout = sys.stdout
    old_stderr = sys.stderr

    with io.StringIO() as str_buff:
        sys.stdout = str_buff
        sys.stderr = str_buff
        try:
            exec(cmd)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        data = str_buff.getvalue().strip()

    await ctx.send(data if data else 'No output.')


with open('token.txt') as fp:
    token = fp.read().strip()

try:
    bot.run(token)
except KeyboardInterrupt:
    exit(0)
