import discord
import re

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("comes here")
    print(message.author.name)
    if message.author == client.user:
        return # to prevent bot form kicking itself
    evil_user = "navoneel"
    print(type(message.author.name))
    if re.search(evil_user, message.author.name):
        await message.author.guild.kick(message.author)
        await message.channel.send(f'navoneel can fuck off!')

        

client.run(<bot_token>)