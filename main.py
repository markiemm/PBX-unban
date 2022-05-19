import re
import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')


@bot.command()
async def unblock(message, ip_addr):
    # Check if `ip_addr` is valid
    if bool(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip_addr)) is True:

        await message.channel.send("Unblocking your IP...")

        try:
            os.system("fwconsole firewall trust " + input)
            await message.channel.purge(limit=999)
            await message.channel.send(":slight_smile: Unblocked Your IP")

        except Exception as e:
            await message.channel.send(f"**Error:** ```{e}```")

    else:
        await message.channel.purge(limit=999)
        await message.channel.send("Not valid")


@bot.event
async def on_ready():
    print(f'[*] Discord.py API Version: {discord.__version__}')
    print(f'[*] Logged in as {bot.user} | {bot.user.id}')


bot.run("")
