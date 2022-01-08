import discord
from discord.ext import commands
import random

player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
client = commands.Bot(command_prefix = '$')

win_conditions = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [0, 3, 6],
                  [1, 4, 7],
                  [2, 5, 8],
                  [0, 4, 8],
                  [2, 4, 6]]
@client.event
async def on_ready():
  print("Ready")

@client.command()
async def tictactoe(ctx, p1:discord.Member, p2:discord.Member):
  global player1 
  global player2
  global turn
  global gameOver
  global count
  print("1")
  if gameOver:
    global board
    board = [':white_large_square:', ":white_large_square:", ":white_large_square:",
             ":white_large_square:", ":white_large_square:", ":white_large_square:",
              ":white_large_square:", ":white_large_square:", ":white_large_square:"]
    turn = ''
    gameOver = False
    count = 0

    player1 = p1
    player2 = p2

    line = ""

    for x in range(len(board)):
      print(x)
      if x == 2 or x == 5 or x==8:
        line += " " + board[x]
        print(line + "2")
        await ctx.send(line)
        line = ""
      else:
        
        line +=  " "+ board[x]
        print(line)

    num = random.randint(1,2)
    if num == 1:
      await ctx.send("It's <@"+ str(player1.id) + ">'s turn'")
      turn = player1
    else:
      turn = player2
      await ctx.send("It's <@" + str(player2.id) + ">'s turn'")

@client.command()
async def p(ctx, pos:int):
  mark = ""
  print('1')
  global player1
  global player2
  global turn
  global board
  global turn
  global gameOver
  global count 
  global win_conditions
  
  print(pos)

  if not gameOver:
    if turn == ctx.author:
      if turn == player1:
        mark = ":regional_indicator_x:"
      elif turn == player2:
        mark = "🅾️"
      
      if 0< pos < 10 and board[pos-1] == ":white_large_square:":
        board[pos - 1] = mark
        count += 1
        line = ""
        for x in range(len(board)):
          if x==2 or x==5 or x==8:
            line += " " + board[x]
            await ctx.send(line)
            line = ""
          else:
            line += " " + board[x]
        checkforWinner(mark, win_conditions)
        print(count)

        if gameOver:
          await ctx.send(mark +"Wins!")
        elif count >= 9:
          gameOver = True
          await ctx.send("It's a tie")
        
        if turn == player1:
          turn = player2
        elif turn == player2:
          turn = player1

      else:
        await ctx.send("Please choose a integer between 1 and 9(both inclusive) on an unmarked tile")
    else:
      await ctx.send("It's not your turn.")
  else:
    await ctx.send("Start a new game using the !tictactoe command")

def checkforWinner(mark, winning_conditions):
  global gameOver

  for i in winning_conditions:
    if board[i[0]] == mark and board[i[1]] == mark and board[i[2]] == mark:
      gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention two players for this command")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to mention/ping players <@")

client.run("OTI4NTkwMjQ5MjIxODMyNzA0.Yda_Dw.pfSGFGmIlqxbVl5TZOitr_Tkwfg")