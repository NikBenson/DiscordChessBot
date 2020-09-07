import os

import discord
from dotenv import load_dotenv
import mysql.connector
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print()


client.run(TOKEN)
