import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send('What do you want me to do?')

client.run('NzQ4MDA4MjkwODk3NzU2MjIw.X0XLAQ.fTgQUGbnfRL47an9YNSFYDQbQdE')