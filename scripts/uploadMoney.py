import json
from scripts.infoForpy import *
import random


@commands.command(pass_context=True)
async def moneyup(ctx, sum):
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
        with open(f'{path}{ctx.message.author.id}.json', 'w') as f:
            f.write(userid_write)
    if (int(useridauthor['money']) >= int(sum)):

        try:
            dictionary = {
                "xp": useridauthor["xp"],
                "access": useridauthor["access"],
                "bank": int(useridauthor["bank"]) + int(sum),
                "money": int(useridauthor['money']) - int(sum)
            }
        except:
            dictionary = {
                "xp": 0,
                "access": 1,
                "bank": 0,
                "money": 0
            }

        userid_write = json.dumps(dictionary, indent=4)

        with open(f"{path}{ctx.message.author.id}.json", "w") as f:
            f.write(userid_write)


        embed = discord.Embed(title="Приват24 (Приват Банк (ДС))",
                              description=f"***Успішно поповненно картку: {ctx.message.author.id} на суммою: {sum}₴***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Поповнено Картку",
                        value=f"***{ctx.message.author.id}***",
                        inline=False)
        embed.add_field(name="На сумму", value=f"{sum}₴",

                        inline=False)
        embed.add_field(name="З комісією", value=f"0₴",
                        inline=False)

        await ctx.send(embed=embed)
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
    else:
        embed = discord.Embed(title="Термінал (Приват Банк (ДС))",
                              description=f"***Вибачте, але у вас недостатньо коштів щоби поповнити картку: {ctx.message.author.id} на сумму: {sum}₴.***",
                              color=0xFF5733)
        await ctx.send(embed=embed)