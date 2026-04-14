import psutil
import discord

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import Message, Client

async def status(bot: "Client", msg: "Message"):
    embed = discord.Embed(
        title="PC Stats",
        color=discord.Color.fuchsia(),
        type="rich",
        description=f""
    )
    await msg.channel.send(embed=embed)