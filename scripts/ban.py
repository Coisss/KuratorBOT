from scripts.infoForpy import *


@commands.command(pass_context=True)
async def ban(ctx, user: discord.Member, *,reason):
    try:

        with open(f'{path}{ctx.message.author.id}.json', 'r') as f:
            useridauthor = json.load(f)
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

    if(int(useridauthor['access'] >= 3)):
        embed = discord.Embed(title="Бан",
                              description=f"***Ви заблокували користувача: {user.mention}, з причиною: {reason}.***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Адмін", value=f"{ctx.message.author.mention}",

                        inline=False)
        embed.add_field(name="З причиною",
                        value=f"***{reason}***",
                        inline=False)
        await user.send(embed=embed)
        await user.ban(reason=reason)

        await ctx.send(embed=embed)

        print(f"Created a {user.id} kick_DB!")
        dictionary = {
            "reason": reason,
            "adminid" : str(ctx.message.author.id),
            "adminment": str(ctx.message.author.mention)
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{ban_dbpath}{user.id}.json', 'w') as f:
            f.write(userid_write)
    else:
        embed = discord.Embed(title="Бан",
                              description=f"***Не вдалося Заблокувати користувача: {user.mention}.***",
                              color=0xFF5733)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar.url)
        embed.add_field(name="Причина", value=f"Не достатньо прав!",

                        inline=False)
        await ctx.send(embed=embed)




