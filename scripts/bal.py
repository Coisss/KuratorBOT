import json
from scripts.infoForpy import *


@commands.command()
async def bal(ctx, user: discord.Member):
    global useridauthor
    global userid
    print(ctx.message.author.id)
    try:

        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)

    except:
        print(f"Created a {ctx.message.author.id} database!")

    try:

        with open(f'{path}{user.id}.json', 'r') as f:
            userid = json.load(f)

            embed = discord.Embed(title="Приват24 (Приват Банк (ДС))",
                                  description=f"***Баланс картки: {user.id}***",
                                  color=0xFF5733)
            embed.set_author(name=user.name, icon_url=user.avatar.url)
            embed.add_field(name="Фінанси на Картці", value=f"{userid['bank']}₴",

                            inline=False)
            embed.add_field(name="Фінанси на Руках", value=f"{userid['money']}₴",
                            inline=False)
            embed.add_field(name="Як закидувати на картки й снімати з карток?", value=f"***.moneyup 50 - положити на картку гроші. .bankget 50 - взяти з картки гроші.***",
                            inline=False)
            await ctx.send(embed=embed)


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





