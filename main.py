from discord.ext import commands
import discord
from datetime import datetime
import os
import json

prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("bot is ready")



@bot.command()
async def setup(ctx, setupType, setupInfo):
    if f"{ctx.guild.id}.json" not in os.listdir("servers"):
        with open(f"servers/{ctx.guild.id}.json", "w") as f:
            json.dump({"logs_channel": "", "suggestion_channel": ""}, f)
    if str(setupType) == "logs":
        print(ctx.guild.id)

        logsChannel = setupInfo.split("#")[1].split(">")[0]

        print(logsChannel)
        x = bot.get_channel(int(logsChannel))
        print(x)






bot.run("NzU1MDU5ODQxNzk3NzE4MDU2.X19yRg.xEmjXNdHAQkyyeKAtFZ0CLttquI")
