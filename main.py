import re
import subprocess

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')


def _run_system_command(command: list, show: bool = False):
    """
    Execute a system command properly

    Args:
        command (list): Command as a list
        show (bool, optional): Print out the output. Defaults to False.

    Returns:
        code, out, err
    """
    p = subprocess.run(command, capture_output=True, text=True)
    code, out, err = p.returncode, p.stdout, p.stderr
    if show:
        print(out or err)
    return code, out, err


@bot.command()
async def unblock(message, ip_addr):
    # Check if `ip_addr` is valid
    if bool(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip_addr)) is True:

        # Inform user that the process is starting
        await message.channel.send("Unblocking your IP...")

        try:
            # Execute the system command
            code, out, err = _run_system_command(
                command=["fwconsole", "firewall", "trust", str(ip_addr)])

            # Delete the messages in the channel
            await message.channel.purge(limit=999)

            # Comment the code below if you dont want to send the output
            await message.channel.send(
                f"**Return Code:** `{code}`\n**Output:** ```{out or err}```"
            )

            # Inform the user that the process is completed
            await message.channel.send(":slight_smile: Unblocked Your IP")

        except Exception as e:
            # Send the exception if anything goes wrong
            await message.channel.send(f"**Error:** ```{e}```")

    # If `ip_addr` is NOT valid
    else:
        await message.channel.purge(limit=999)
        await message.channel.send("Not valid")


@bot.event
async def on_ready():
    print(f'[*] Discord.py API Version: {discord.__version__}')
    print(f'[*] Logged in as {bot.user} | {bot.user.id}')


bot.run("")
