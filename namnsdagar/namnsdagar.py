import requests
import re
import os

response = requests.get("https://svenskanamn.se/namnsdagar/")
response.encoding = "utf-8"
text = response.text
namelist = re.split("/namn/",text)
final = []
for name in namelist[1:-2]:
    temp = name.split("/")
    final.append(temp[0][:1].upper() + temp[0][1:])

dir_path = "C:\\Users\\felix\\Documents\\random"
logopath = "C:\\Users\\felix\\Pictures\\icons\\trumpet29.svg"
generatedscript = open(dir_path + "\\" + "burnttoastscript.ps1", "w")
generatedscript.writelines("New-BurntToastNotification ")
generatedscript.writelines("-Text \"Daglig kungörelse\", ")

if len(final) == 1:
    generatedscript.writelines("\'Idag har " + final[0] + "namnsdag.\'")
elif len(final) == 2:
    generatedscript.writelines("\'Idag har " + final[0] + " och " + final[1] + " namnsdag.\'")

generatedscript.writelines(" -AppLogo " + logopath)