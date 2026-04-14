# for intellisense
import discord
from models import Routines
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import Message, Client

async def routine(bot: "Client", msg: "Message"):
    mat = re.match(r"^!obs (?P<msg>[a-zA-Z_]+) (?P<content>[a-zA-Z 0-9]+)$", msg.content)
    # print(mat.group("content")) # type: ignore
    if mat and mat.group("content"):
        Routines.insert(user_id=msg.author.id, routine_content=mat.group("content")).on_conflict_replace().execute()
        await msg.channel.send("Added to your routines :white_check_mark:")
    else:
        await msg.channel.send("Invalid message syntax")