import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

intents = discord.Intents.default()

intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():

  print("Created by Arun") 
  print(client.user.name)
  print("-------")

@client.event
async def on_member_join(member):

  guild = client.get_guild(767653647734538251) 
  channel = guild.get_channel(767653647734538255)
  await channel.send(f'Welcome to the server {member.mention}')
  
  #embed=discord.Embed(title="welcome !",color=0x9208ea, description=f"{member.mention} Just Joined!")

  #embed.set_footer(text="Made by Arun") 


  #await message.channel.send(discord.Object(id="926454481762263043"), embed=embed)
  #await message.channel.send('Hello There!')


client.run("OTI4MTkzOTA2NTIzNDAyMjUw.YdVN8A.qbB0LMYZDYTkFfPu1wr5IeHgb7U")