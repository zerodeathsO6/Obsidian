import discord
from typing import TYPE_CHECKING
from models import Routines
if TYPE_CHECKING:
     from discord import Message, Client

async def remove_routine(bot: "Client", msg: "Message"):
    Routines.delete_by_id(msg.author.id)
    await msg.channel.send("Deleted")