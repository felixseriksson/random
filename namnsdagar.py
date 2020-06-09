import requests
import re

response = requests.get("https://svenskanamn.se/namnsdagar/")
response.encoding = "utf-8"
text = response.text
namelist = re.split("/namn/",text)
final = []
for name in namelist[1:-2]:
    temp = name.split("/")
    final.append(temp[0])
