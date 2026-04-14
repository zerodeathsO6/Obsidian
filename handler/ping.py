# for intellisense
import discord

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import Message, Client

async def ping(bot: "Client", msg: "Message"):
    embed = discord.Embed(
        title="Ping",
        description="Hello world",
        color=discord.Color.blue()
    )
    await msg.channel.send(embed=embed)