import json
from pythonProject.scripts.infoForpy import *
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
from pythonProject.scripts.addrole import *
from pythonProject.scripts.paymoney import *
from pythonProject.scripts.setxp import *
from pythonProject.scripts.addxp import *
from pythonProject.scripts.remrole import *
from pythonProject.scripts.bal import *
from pythonProject.scripts.payb import *
from pythonProject.scripts.getMoney import *
from pythonProject.scripts.uploadMoney import *
from pythonProject.scripts.kick import *
from pythonProject.scripts.ban import *

import os

def Start():

    discord.Guild.unban(self= 850992845371211786, user= 850992845371211786)
    bot.add_command(addxp)
    bot.add_command(addrole)
    bot.add_command(removerole)
    bot.add_command(setxp)
    bot.add_command(bal)
    bot.add_command(paym)
    bot.add_command(payb)
    bot.add_command(bankget)
    bot.add_command(moneyup)
    bot.add_command(kick)
    bot.add_command(ban)



    LEGION = "MTA0MzkwMTA3ODc1Mzc4Nzk0NQ.GGl46i.brZ6O1EpIfq911fJFqukqGSlTQNjkQDR-rDoEc"
    KuratorBOT = "MTA0MzkwMTA3ODc1Mzc4Nzk0NQ.GGl46i.brZ6O1EpIfq911fJFqukqGSlTQNjkQDR-rDoEc"
    bot.run(KuratorBOT)