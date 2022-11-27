import json
import discord
from discord import embeds
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context


ban_dbpath = "C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/users/ban_db/"
kick_dbpath = "C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/users/kick_db/"
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
path = "C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/users/database/"
path_lang = "C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/config/language/"
path_lang_opt = "C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/config/"

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

with open(f'C:/Users/UTF-8/Desktop/PycharmProjects/pythonProject/access.json', 'r') as f:
    access = json.load(f)

if(what_lang_cur["what_language_to_use"] == "ukr"):
    cur_lang = ukr
if (what_lang_cur["what_language_to_use"] == "ru"):
    cur_lang = ru


bot = Bot(command_prefix=".", intents=intents, help_command=None)


