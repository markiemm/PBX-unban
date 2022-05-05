import discord
from discord import client
from discord import user
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os, re

bot = commands.Bot(command_prefix='?')

@bot.command()
async def unblock(message, input):
    if bool(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", input)) == True:
        await message.channel.send("Unblocking your IP...")
        try:
            os.system("fwconsole firewall trust " + input)
            await message.channel.purge(limit=999)

        except Exception as e:
            await message.channel.send(f"There was an error: {e}")
    else:
        await message.channel.purge(limit=999)
        await message.channel.send("Not valid")

bot.run("")