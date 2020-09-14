from discord.ext import commands
import discord
from datetime import datetime

prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("bot is ready")


async def setupCommand(message, config):
    embed = discord.Embed(title="bot setup", timestamp=datetime.now())
    embed.add_field(name="Please mention or send the Discord ID of the admin role", value="Example: @admin")
    await message.channel.send(embed=embed)

    def check(m):
        if message.author == m.author and m.channel == message.channel:
            return True

    try:
        adminRole = await bot.wait_for('message', check=check, timeout=60)
    except:
        await message.channel.send("Sorry, you took too long!")
        return None
    adminRole = adminRole.content
    try:
        if "&" in adminRole:
            adminRole = adminRole.split("&")[1].split(">")[0]
        adminRole = message.guild.get_role(int(adminRole))
        print(adminRole)
    except:
        await message.channel.send("Sorry, that is not a correct Discord role!")
        return None

    if config == "auto":
        cat = await message.guild.create_category(name="suggestions")
        overwrites = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, add_reactions=False),
            adminRole: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)
        }

        modChannel = await message.guild.create_text_channel('approval-channel', overwrites=overwrites, category=cat)
        overwrites = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False),
            adminRole: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)
        }
        userChannel = await message.guild.create_text_channel('suggestion-channel', overwrites=overwrites, category=cat)


@bot.event
async def on_message(message):
    if message.content.startswith("?setup"):
        if message.content.startswith("?setup auto"):
            await setupCommand(message, 'auto')
        elif message.content.startswith("?setup manual"):
            await setupCommand(message, 'auto')




bot.run("NzU1MDU5ODQxNzk3NzE4MDU2.X19yRg.xGpavfPWuRX9Tl3ggqLgFWsBtP0")
