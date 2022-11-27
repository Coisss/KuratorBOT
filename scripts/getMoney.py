import json
from scripts.infoForpy import *
import random

@commands.command(pass_context=True)
async def bankget(ctx, sum):
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
    if(int(useridauthor['bank']) >= int(sum)):

        try:
            dictionary = {
                "xp": useridauthor["xp"],
                "access": useridauthor["access"],
                "bank" : int(useridauthor["bank"]) - int(sum),
                "money" : int(useridauthor['money']) + int(sum)
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

        embed = discord.Embed(title="Банкомат (Приват Банк (ДС))",
                              description=f"***Успішно знято з картки: {ctx.message.author.id} - {sum}₴***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Знято з картки",
                        value=f"***{ctx.message.author.id}***",
                        inline=False)
        embed.add_field(name="Сумму", value=f"{sum}₴",

                        inline=False)
        embed.add_field(name="При комісії", value=f"0₴",
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
        embed = discord.Embed(title="Банкомат (Приват Банк (ДС))",
                              description=f"***Вибачте, але на картці: {ctx.message.author.id} немає необхідних коштів, а саме: {sum}₴.***",
                              color=0xFF5733)
        await ctx.send(embed=embed)