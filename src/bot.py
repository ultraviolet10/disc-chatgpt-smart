import os
import discord
import openai

openai.api_key = os.environ['OPENAI_API']
disc_secret = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
client = discord.Client(intents=intents)


def generate_response(prompt):
    model_engine = "text-davinci-002"
    prompt = (f"{prompt}")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()


@client.event
async def on_ready():
    print('Chat-terjee online, logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        prompt = message.content[5:]
        response = generate_response(prompt)

        # Send the response back to the user
        await message.channel.send(response)


client.run(disc_secret)
