import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name}')

@bot.event
async def on_message(message):
    # Avoid the bot responding to its own messages to prevent infinite loops
    if message.author == bot.user:
        return
    
    # Ensure that the bot only performs actions when users send messages starting with 'https://twitter.com' or 'https://x.com/'.
    if message.content.startswith(('https://twitter.com/', 'https://x.com/')):
        # Replace the part of the message with 'https://twitter.com/' or 'https://x.com/' with 'https://fxtwitter.com/', ensuring embedded tweets display correctly in Discord.
        finalMessage = message.content.replace('https://twitter.com/', 'https://fxtwitter.com').replace('https://x.com/', 'https://fxtwitter.com')
        
        # Send back the new message to the same Discord channel from which the original message was sent.
        await message.channel.send(finalMessage)
        
    # Allow other message events to work correctly with the bot:
    await bot.process_commands(message)

# Run the bot with the token retrieved from the environment variable
bot.run(TOKEN)
