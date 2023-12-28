import discord
from discord.ext import commands

TOKEN = 'MTE4OTk2MDE0NTk1MDc0ODc1Mg.GjA09u.Ta5WCoL1otb86z4wI_XhNN1jZO17Vrc40IgUMI'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    
    # By using this if statement, we prevent the bot from responding to its own messages, thus avoiding infinite loops.
    if message.author == bot.user:
        return
    
    # We'll ensure that the bot only performs its actions when users send messages starting with 'https://twitter.com' or 'https://x.com'.
    
    if message.content.startswith(('https://twitter.com/', 'https://x.com/')):
        # We replace the part of the message with 'https://twitter.com' or 'https://x.com' with 'https://fxtwitter.com', ensuring embedded tweets display correctly in Discord.
        finalMessage = message.content.replace('https://twitter.com/', 'https://fxtwitter.com').replace('https://x.com/', 'https://fxtwitter.com')
        
        # And send back the new message to the same Discord channel from which the original message was sent.
        await message.channel.send(finalMessage)
        
    # To allow other message events to work correctly with the bot:
    
    await bot.process_commands(message)
    
bot.run(TOKEN)