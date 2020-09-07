import os

import discord
from dotenv import load_dotenv
import mysql.connector
import requests

mydb = mysql.connector.connect(
  host="localhost",
  user="laravel",
  password="awsxdrfvgz"
)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('connected!')


@client.event
async def on_member_join(member):
    if(True): #member.id):
        await member.create_dm()
        await member.dm_channel.send(
            f"Please link your lichess account in order to use this bot. https://my.link.com/?discord_id={member.id}"
        )

client.run(TOKEN)
