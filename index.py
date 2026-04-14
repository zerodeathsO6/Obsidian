import discord
import re
import logic
from peewee import SqliteDatabase
from models import db_proxy, Routines
from dotenv import dotenv_values

privs = dotenv_values(".env")

# handler logic
cmds = logic.handler()


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = SqliteDatabase("bot.db")
        db_proxy.initialize(self.db)
        self.db.connect()
        self.db.create_tables([Routines])

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if content := re.match(r"^!obs (?P<msg>[a-zA-Z_]+).*$", message.content):
            cmd = cmds.get(content.group("msg"))
            await cmd(self, message) # type: ignore
        else:
            await message.channel.send("No command found")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(privs["TOKEN"]) # type: ignore
