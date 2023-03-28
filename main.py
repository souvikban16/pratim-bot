from bot import bot

import discord
import re


class MyClient(discord.Client):

  #@client.event
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))

  #@client.event
  async def on_message(message):
    print("comes here")
    print(message.author.name)
    if message.author == client.user:
      return  # to prevent bot form kicking itself
    evil_user = "navoneel"
    print(type(message.author.name))
    if re.search(evil_user, message.author.name):
      await message.author.guild.kick(message.author)
      await message.channel.send(f'navoneel can fuck off!')


intents = discord.Intents.default()
intents.message_content = True
bot()

client = MyClient(intents=intents)
client.run(
  '')
