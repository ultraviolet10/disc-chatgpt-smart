import os
import discord

disc_secret = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Chat-terjee online, logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.guild.id == 1055780464507502592:
        print('in')
        print(message.content)
        if message.author == client.user:
            print('not here')
            return
        if message.content.startswith('$hello'):
            print('true')
            await message.channel.send('Hello.')


client.run(disc_secret)
