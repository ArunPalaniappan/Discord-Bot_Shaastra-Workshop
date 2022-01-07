import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command
async def on_ready():

  print("Created by Arun") 
  print(client.user.name)
  print("-------")

@bot.command() 
async def add(ctx, num1, num2):
  await ctx.reply(float(num1)+float(num2))

@bot.command() 
async def sub(ctx, num1, num2):
  await ctx.reply(float(num1)-float(num2))

@bot.command() 
async def mul(ctx, num1, num2):
  await ctx.reply(float(num1)*float(num2))

@bot.command() 
async def div(ctx, num1, num2):
  await ctx.reply(float(num1)/float(num2))

bot.run('OTI3OTE3Njk2OTkyMDM4OTc1.YdRMsg.ZdnVcbJ0aRgpJEKwRRBGAsGeQ58')