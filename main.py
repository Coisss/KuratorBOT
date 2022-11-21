import json
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context


intents = discord.Intents.default()
intents.message_content = True
path = "users/database/"
path_lang = "config/language/"
path_lang_opt = "config/"

useridauthor = ""
userid = ""
userid_write = ""

ru = "ss"
ukr = "ss"
what_lang_cur = "ss"
cur_lang = "ss"



with open(f'{path_lang_opt}language_options.json', 'r', encoding="utf-8") as f:
    what_lang_cur = json.load(f)

with open(f'{path_lang}language_ru.json', 'r', encoding="utf-8") as f:
    ru = json.load(f)


with open(f'{path_lang}language_uk.json', 'r', encoding="utf-8") as f:
    ukr = json.load(f)

with open(f'access.json', 'r') as f:
    access = json.load(f)

if(what_lang_cur["what_language_to_use"] == "ukr"):
    cur_lang = ukr
if (what_lang_cur["what_language_to_use"] == "ru"):
    cur_lang = ru


bot = Bot(command_prefix=".", intents=intents, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing( ))
"""

IDS = 0


# Opening JSON file
with open('totid.json', 'r') as openfile:
    json_object = json.load(openfile)

IDS = json_object['ti']
IDS = IDS + 1
dictionary = {
    "xp": 56
}



dictionary2 = {
    "ti": IDS
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
json_object2 = json.dumps(dictionary2, indent=4)

with open(f"totid.json", "w") as outfile:
    outfile.write(json_object2)



with open(f"{str(IDS)}.json", "w") as outfile2:
    outfile2.write(json_object)
"""



@commands.command(pass_context=True)
async def setxp(ctx, arg1, arg2):
    global useridauthor
    global userid
    try:
        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{ctx.message.author.id}")
    try:
        with open(f'{path}{arg1}.json', 'r') as f:
            userid = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{arg1}")

    if int(useridauthor["access"]) >= 3:
        try:
            dictionary = {
                "xp": int(arg2),
                "access": userid["access"],
                "mute_status" : userid["mute_status"],
                "mute_second" : userid["mute_second"]
            }
        except:
            dictionary = {
                "xp": 0,
                "access": 1,
                "mute_status" : 0,
                "mute_second" : 0
            }


        userid_write = json.dumps(dictionary, indent=4)

        with open(f"{path}{arg1}.json", "w") as f:
            f.write(userid_write)

        await ctx.send(f"{cur_lang['setxp1']}{arg1} {cur_lang['setxp2']}{arg1}!")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")

@commands.command(pass_context=True)
async def addxp(ctx, arg1, arg2):


    global useridauthor
    global userid
    try:
        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{ctx.message.author.id}")
    try:
        with open(f'{path}{arg1}.json', 'r') as f:
            userid = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{arg1}")


    if int(useridauthor["access"]) >= 3:
        try:
            dictionary = {
                "xp": int(userid["xp"]) + int(arg2),
                "access": userid["access"],
                "mute_status" : userid["mute_status"],
                "mute_second" : userid["mute_second"]
            }
        except:
            dictionary = {
                "xp": 0,
                "access": 1,
                "mute_status" : 0,
                "mute_second" : 0
            }

        userid_write = json.dumps(dictionary, indent=4)
        with open(f"{path}{arg1}.json", "w") as f:
            f.write(userid_write)
        print(f"{cur_lang['addxp1']}{arg1} {cur_lang['addxp2']}{arg1}!")
        await ctx.send(f"{cur_lang['addxp1']}{arg1} {cur_lang['addxp2']}{arg1}!")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")


@commands.command(pass_context=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    print(ctx.message.author.id)
    global useridauthor
    try:
        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
    except:
        print(f"{cur_lang['db_created']}{ctx.message.author.id}")

    if(useridauthor["access"] >= 3):
        try:
            await user.add_roles(role)
            await ctx.send(f"{cur_lang['rolegive1']}{role}, {cur_lang['rolegive2']}{user}.")
        except:
            await ctx.send(f"{cur_lang['botmissingperms']}")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")

@bot.event
async def on_message(message: discord.Message) -> None:
    print(f"{message.created_at}  | {message.author}  |   {message.content} ")
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)
    dictionary = {
        "xp": 0,
        "access": 1,
        "mute_status": 0,
        "mute_second": 0
    }
    userid_write = json.dumps(dictionary, indent=4)
    try:
        with open(f"{path}{str(message.author.id)}.json", "r") as f:
            f = json.load(f)
    except:
        with open(f"{path}{str(message.author.id)}.json", "w") as f:
            f.write(userid_write)

    dictionary2 = "ss"


    if(f["mute_status"] == 1):


        message.delete()
        for i in range(1,f["mute_second"]):
            dictionary2 = {
                "xp": f["xp"],
                "access": f["access"],
                "mute_status": f["mute_status"],
                "mute_second": int(f["mute_second"]) - 1
            }
    if(int(f["mute_second"]) > 0):
        dictionary2 = {
            "xp": f["xp"],
            "access": f["access"],
            "mute_status": 1,
            "mute_second": f["mute_second"]
        }

    userid_write2 = json.dumps(dictionary2, indent=4)


    userid_write = json.dumps(dictionary, indent=4)
    try:
        with open(f"{path}{str(message.author.id)}.json", "r") as f:
            f.write(userid_write2)
    except:
        with open(f"{path}{str(message.author.id)}.json", "w") as f:
            f.write(userid_write)
            print(f"{cur_lang['db_created']}{message.author.id}")

@commands.command()
async def removerole(ctx, user: discord.Member, role: discord.Role):
    global useridauthor
    try:

        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
            print("cool!")
    except:
        print(f"Created a {ctx.message.author.id} database!")

    if(useridauthor["access"] >= 3):
        try:
            await user.remove_roles(role)
            await ctx.send(f"{cur_lang['rolerem1']}{role}, {cur_lang['rolerem2']}{user}.")
        except:
            await ctx.send(f"{cur_lang['botmissingperms']}")
    else:
        await ctx.send(f"{cur_lang['user_missing_perms']}")

bot.add_command(addxp)
bot.add_command(addrole)
bot.add_command(removerole)
bot.add_command(setxp)



bot.run("MTA0MzkwMTA3ODc1Mzc4Nzk0NQ.Gg9JSz.3uuFH8RUkK57Q7bXlqVSzmlAPKPeRwf-M9pMIA")