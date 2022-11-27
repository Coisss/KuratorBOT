import json
from scripts.infoForpy import *

@commands.command()
async def payb(ctx, user: discord.Member, sum):

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

    if(int(useridauthor['bank']) >= int(sum) ):
        dictionary1 = {
            "xp": int(userid['xp']),
            "access": userid["access"],
            "bank": int(userid["bank"]) + int(sum),
            "money": userid["money"]
        }
        dictionary2 = {
            "xp": useridauthor["xp"],
            "access": useridauthor["access"],
            "bank": int(useridauthor["bank"]) - int(sum),
            "money": useridauthor["money"]
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

        embed = discord.Embed(title="Приват24 (Приват Банк (ДС))",
                              description=f"***Успішно пересланно гроші на рахунок Картки: {ctx.message.author.id} з суммою: {sum}₴***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Поповнено Картку",
                        value=f"***{user.id}***",
                        inline=False)
        embed.add_field(name="На сумму", value=f"{sum}₴",

                        inline=False)
        embed.add_field(name="З комісією", value=f"0₴",
                        inline=False)

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Приват24 (Приват Банк (ДС))",
                              description=f"***Вибачте, але у вас недостатньо коштів на вашій картці, щоби поповнити картку: {ctx.message.author.id} на сумму: {sum}₴.***",
                              color=0xFF5733)
        await ctx.send(embed=embed)