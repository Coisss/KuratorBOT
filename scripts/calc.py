import json
from scripts.infoForpy import *
import random

isAnsweredGreat = ""
isAnswering = False
res = 0
x = 0
y = 0
z = ""
operations = ["+", "-", "*", "/", "%"]
@commands.command(pass_context=True)
async def math(ctx):
    x = random.randint(0,100)
    y = random.randint(0, 100)
    z = random.choice(operations)

    if(z == "+"):
        print(x + y)
        res = x + y

    if(z == "-"):
        print(x - y)
        res = x - y

    if(z == "*"):
        print(x * y)
        res = x * y

    if(z == "/"):
        print(x / y)
        res = x / y

    if (z == "%"):
        print(x % y)
        res = x % y

    await ctx.send(f"**PROBLEM 1: {str(x)} {z} {str(y)} = ?**")
    await ctx.send(f"***... TIP: Use a .math2 answer. Example: .math2 56 ...***")


@bot.event
async def Change(ctx):
    isAnswering = True
    if(isAnsweredGreat == True):
        await ctx.send("You did this! you can have that 1 xp!")
    elif(isAnsweredGreat == False):
        await ctx.send(f"NO, the {str(x)} {z} {str(y)}, is going to be {str(res)}!")

