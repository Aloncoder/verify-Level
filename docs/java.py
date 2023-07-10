import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Allow receiving messages with file attachments

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.event
async def on_message(message):
    # Check if the message contains a file attachment
    if message.attachments:
        file_url = message.attachments[0].url
        discord_name = message.content
        channel_id = 1058057737277276313  # Replace with your desired channel ID
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(f'File URL: {file_url}, Discord Name: {discord_name}')
        else:
            print(f'Invalid channel ID: {channel_id}')
    
    await bot.process_commands(message)

bot.run('MTA4ODEwMjA3NTY2NzMzMzE2Mg.GGfbai.zMD_XNNHh7uoAUoeCgzhZsetLaM9PhoChQF9NQ')
