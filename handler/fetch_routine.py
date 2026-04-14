# for intellisense
import discord
from models import Routines
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import Message, Client

async def fetch_routines(bot: "Client", msg: "Message"):
    try:
        get: Routines = Routines.get_or_none(user_id=msg.author.id)
        embed = discord.Embed(
            title="Routines",
            description=get.routine_content,
            timestamp=get.time # type: ignore
        )
        await msg.channel.send(embed=embed)
    except:
        await msg.channel.send("Could not find a routine, perhaps try adding one")
