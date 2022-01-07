import os
import discord

alpha = ['😋','😆', '😆' ]
class Client(discord.Client):
  
  def __init__(self, *args, **kwargs):
    super().__init__( *args, **kwargs)
    self.target_message_id = 927523464305344512
  async def on_ready(self):
    print("Ready")

  async def on_raw_reaction_add(self, payload):
    
    if payload.message_id != self.target_message_id:
      return

    guild = client.get_guild(payload.guild_id)
    print(payload.emoji.name)
    if payload.emoji.name in alpha:
      role = discord.utils.get(guild.roles, name = 'Alpha') 
      await payload.member.add_roles(role)

  async def on_raw_reaction_remove(self, payload):
    if payload.message_id != self.target_message_id:
      return
    guild = client.get_guild(payload.guild_id)
    if payload.emoji.name in alpha:
      role = discord.utils.get(guild.roles, name = 'Alpha') 
      await payload.member.add_roles(role)


intents = discord.Intents.default()
intents.members = True

client = Client(intents=intents)
client.run("OTI3NDMyMzc3MzMwOTg3MDQ5.YdKItQ.1A8j7_7pv-YX_Z87sDvMB-Yl5_M")