import json

import discord

from scripts.command_reg import Start
from scripts.infoForpy import *
import os



@bot.event
async def on_message(message: discord.Message) -> None:
    print(f"{message.created_at}  | {message.author}  |   {message.content} ")
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)

    try:
        with open(f"{path}{str(message.author.id)}.json", "r") as f:
            f = json.load(f)
    except:
        dictionary = {
            "xp": 0,
            "access": 1,
            "bank": 0,
            "money": 0
        }
        userid_write = json.dumps(dictionary, indent=4)
        with open(f'{path}{message.author.id}.json', 'w') as f:
            f.write(userid_write)
@bot.event
async def on_member_join(member):
    await member.guild.unban()
    ban_id_path = ban_dbpath + str(member.id) + ".json"
    bdc = ""
    if os.path.isfile(ban_id_path):

        with open(ban_id_path, "r") as f:
            bdc = json.load(f)

        embed = discord.Embed(title=f"Команда Проєкту {member.guild.name}",
                              description=f"***Ви заблоковані на нашому проєкті: {member.guild.name}!***",
                              color=0xFF5733)
        embed.add_field(name="Адмін", value=f"{bdc['admin']}",

                        inline=False)
        embed.add_field(name="З причиною",
                        value=f"***{bdc['reason']}***",
                        inline=False)
        await member.send(embed=embed)
        if os.path.isfile(ban_id_path):
            os.remove(ban_id_path)
            print(f'Haved a kick info file in directiory: {ban_id_path}.')
            print('attemp to remove it...')
            print('removed!')
        else:
            print('passed')
    elif not os.path.isfile(ban_id_path):
        await member.guild.unban()


    else:
        invites = await member.guild.invites()
        x = " "
        for x in invites:
            print(f"Total uses: {x.uses} Created by: {x.inviter}")
        embed = discord.Embed(title=f"Команда Проєкту {member.guild.name}",
                              description=f"***Ласкаво Просимо, на сервер: {member.guild.name}.***",
                              color=0xFF5733)
        embed.add_field(name="Пригласив", value=f"{x.inviter}",

                        inline=False)
        embed.add_field(name="Кого", value=f"{member.mention}",
                        inline=False)
        embed.add_field(name="Всього використань цього інвайту",
                        value=f"***{str(x.uses)}***",
                        inline=False)
        await member.send(embed=embed)
        kick_id_path = kick_dbpath + str(member.id) +".json"
        print(kick_id_path)
        if os.path.isfile(kick_id_path):
            os.remove(kick_id_path)
            print(f'Haved a kick info file in directiory: {kick_id_path}.')
            print('attemp to remove it...')
            print('removed!')
        else:
            print('passed')

Start()









