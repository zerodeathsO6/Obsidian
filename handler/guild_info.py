async def guild_info(bot, msg):
    await msg.channel.send(msg.guild.id)