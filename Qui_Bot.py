import discord
import asyncio
import random

client = discord.Client()

dic = [{'title': 'What year is it?', 
        'answer': [{'answer':'2020','is_correct': False},
                   {'answer':'2021','is_correct': False},
                   {'answer':'2022','is_correct': True}]}]


def get_question():
    qs = ''
    id = 1
    answer = 0
    list1 = [0]
    n = int(random.choice(list1))
    qs += "Question: \n"
    qs += dic[n]['title'] + "\n"

    for item in dic[n]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id

        id += 1

    return (qs, answer)

@client.event
async def on_ready():

  print("Created by Arun") 
  print(client.user.name)
  print("-------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$question'):

        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit() 
        
        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Time is up!')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('Oops. That is not right!')
        
client.run('OTI4MjY2NDc5ODY1MDUzMjI0.YdWRhw.4yETWZ-yVjBwNXuoeUfq3m7suh8')
