import json
from scripts.infoForpy import *

@commands.command(pass_context=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    print(ctx.message.author.id)
    global useridauthor
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
        with open(f'{path}{user.id}.json', 'w') as f:
            f.write(userid_write)

    if(useridauthor["access"] >= 3):
        try:
            await user.add_roles(role)
            await ctx.send(f"{cur_lang['rolegive1']}{role}, {cur_lang['rolegive2']}{user}.")
        except:
            await ctx.send(f"{cur_lang['botmissingperms']}")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")
