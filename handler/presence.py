import discord
import re
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from discord import Message, Client

async def presence(bot: "Client", msg: "Message"):
    match = re.match(r"^!obs (?P<msg>[a-zA-Z_]+) (?P<presence>idle|dnd|online|offline)$" ,msg.content)
    if match:
         if prs := match.group("presence"):
              match prs:
                   case "idle":
                        await bot.change_presence(status=discord.Status.idle)
                   case "dnd":
                        await bot.change_presence(status=discord.Status.dnd)
                   case "online":
                        await bot.change_presence(status=discord.Status.online)
                   case "offline":
                        await bot.change_presence(status=discord.Status.offline)
              await msg.channel.send("Changed to "+ prs)
         else:
              await msg.channel.send("Invalid presence")
         