import json
from scripts.infoForpy import *

@commands.command()
async def paym(ctx, user: discord.Member, sum):

    global useridauthor
    global userid
    try:

        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
    except:
        print(f"Created a {ctx.message.author.id} database!")
    try:

        with open(f'{path}{user.id}.json', 'r') as f:
            userid = json.load(f)
            print(userid['xp'])
    except:
        print(f"Created a {user.id} database!")
        dictionary = {
            "xp": 0,
            "access": 1,
            "bank": 0,
            "money": 0
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{path}{user.id}.json', 'w') as f:
            f.write(userid_write)

    if(int(useridauthor['money']) >= int(sum)):
        dictionary1 = {
            "xp": int(userid['xp']),
            "access": userid["access"],
            "bank": userid["bank"],
            "money": int(userid["money"]) + int(sum)
        }
        dictionary2 = {
            "xp": useridauthor["xp"],
            "access": useridauthor["access"],
            "bank": useridauthor["bank"],
            "money": int(useridauthor["money"]) - int(sum)
        }
        userid_write = json.dumps(dictionary1, indent=4)
        userid_write2 = json.dumps(dictionary2, indent=4)
        with open(f"{path}{user.id}.json", "w") as f:
            f.write(userid_write)

        with open(f"{path}{ctx.message.author.id}.json", "w") as f:
            f.write(userid_write2)
        try:

            with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
                useridauthor = json.load(f)
        except:
            print(f"Created a {ctx.message.author.id} database!")
        try:

            with open(f'{path}{user.id}.json', 'r') as f:
                userid = json.load(f)
                print(userid['xp'])
        except:
            print(f"Created a {user.id} database!")
            dictionary = {
                "xp": 0,
                "access": 1,
                "bank": 0,
                "money": 0
            }
            userid_write = json.dumps(dictionary, indent=4)
            with open(f'{path}{user.id}.json', 'w') as f:
                f.write(userid_write)

        embed = discord.Embed(title="Платіж",
                              description=f"***Ви передали: {user.mention} - {sum}₴.***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Фінанси на Картці", value=f"{useridauthor['bank']}₴",

                        inline=False)
        embed.add_field(name="Фінанси на Руках", value=f"{useridauthor['money']}₴",
                        inline=False)
        embed.add_field(name="Передано",
                        value=f"***{sum}₴***",
                        inline=False)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Платіж",
                              description=f"***Вибачте, але у вас недостатньо коштів, щоби передати людині: {user.mention} - {sum}₴.***",
                              color=0xFF5733)
        await ctx.send(embed=embed)