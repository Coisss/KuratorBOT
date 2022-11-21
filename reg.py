import json

idsum = "2"

IDs = 2

config = configparser.ConfigParser()
TotalUsers_Get = config.read("ui.ini")
with open(r"ui.ini", 'w') as configfile:
    idsum = configfile["info"]

    IDs = int(idsum['ids'])

config[IDs] = {
    "id" : IDs,
    "nick" : "hgt",
    "xp" : 12
}
IDs = IDs + 1

TotalUsers_Get["info"] = {
    "total_users" : IDs
}

with open(r"ui.ini", 'w') as configfile1:
    TotalUsers_Get.write(configfile1)

with open(fr"{IDs}.ini", 'w') as configfile2:
    config.write(configfile2)