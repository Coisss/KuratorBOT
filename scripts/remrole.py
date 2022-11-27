import json
from scripts.infoForpy import *


@commands.command()
async def removerole(ctx, user: discord.Member, role: discord.Role):
    global useridauthor
    try:

        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
            print("cool!")
    except:
        print(f"Created a {ctx.message.author.id} database!")
        dictionary = {
            "xp": 0,
            "access": 1,
            "bank": 0,
            "money": 0
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{path}{ctx.message.author.id}.json', 'w') as f:
            f.write(userid_write)

    if(useridauthor["access"] >= 3):
        try:
            await user.remove_roles(role)
            await ctx.send(f"{cur_lang['rolerem1']}{role}, {cur_lang['rolerem2']}{user}.")
        except:
            await ctx.send(f"{cur_lang['botmissingperms']}")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")
