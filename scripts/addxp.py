import json

import discord

from scripts.infoForpy import *

@commands.command(pass_context=True)
async def addxp(ctx, arg1: discord.Member, arg2):


    global useridauthor
    global userid
    try:
        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{ctx.message.author.id}")
        dictionary = {
            "xp": 0,
            "access": 1,
            "bank": 0,
            "money": 0
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{path}{ctx.message.author.id}.json', 'w') as f:
            f.write(userid_write)
    try:
        with open(f'{path}{arg1.id}.json', 'r') as f:
            userid = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{arg1.mention}.")
        dictionary = {
            "xp": 0,
            "access": 1,
            "bank": 0,
            "money": 0
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{path}{arg1.id}.json', 'w') as f:
            f.write(userid_write)


    if int(useridauthor["access"]) >= 3:
        try:
            dictionary = {
                "xp": int(userid["xp"]) + int(arg2),
                "access": userid["access"],
                "bank" : userid["bank"],
                "money" : userid["money"]
            }
        except:
            dictionary = {
                "xp": 0,
                "access": 1,
                "bank": 0,
                "money": 0
            }

        userid_write = json.dumps(dictionary, indent=4)
        with open(f"{path}{arg1.id}.json", "w") as f:
            f.write(userid_write)
        print(f"{cur_lang['addxp1']}{arg1} {cur_lang['addxp2']}{arg1.mention}!")
        await ctx.send(f"{cur_lang['addxp1']}{arg2} {cur_lang['addxp2']}{arg1.mention}!")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")
