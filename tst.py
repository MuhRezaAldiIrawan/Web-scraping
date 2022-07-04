import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://ramadan.idntimes.com/'

req = urllib.request.Request(url)
respon = urllib.request.urlopen(req)
responData = respon.read()
import mysql.connector


mysql = mysql.connector.connect(host = 'localhost', 
    password= '', user = 'root', database= 'webscrapping')

mysqlCursor = mysql.cursor()


title = re.findall(r'<h2 class="title-text">(.*?)</h2>', str(responData))
# date = re.findall(r'<time class="date" datetime="2022-04-15">(.*?)</time>', str(responData))

def normalization(text):
    text = text.replace("\\n", " ")
    text = text.replace("\\'", " " )
    text = text.strip()

    return text


# print(title)
# print(date)
# print(category)

for data in range(len(title)):

    gettitle = normalization(title[data])
    # print(normalization(date[data]))

    print(gettitle)

    query = "INSERT INTO ray(title) VALUES('"+gettitle+"')"
    print(query)

    mysqlCursor.execute(query)
    mysql.commit()