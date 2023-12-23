import discord
import random
import asyncio
from discord.ext import commands
import os  # Import the os module

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of random messages
random_messages = [
    "1",
    "2",
]

# Function to send a random message every hour
async def send_random_message():
    channel_id = 1186969403045199933  # Replace with your channel ID
    channel = bot.get_channel(channel_id)

    while not bot.is_closed():
        message = random.choice(random_messages)
        await channel.send(message)
        await asyncio.sleep(3600)  # Sends a message every hour (3600 seconds)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(send_random_message())  # Start the task

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Fetch the bot token from environment variable
bot.run(os.getenv('BOT_TOKEN'))
