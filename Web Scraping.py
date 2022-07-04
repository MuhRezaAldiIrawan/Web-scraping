import urllib.request
from bs4 import BeautifulSoup
import re
import mysql.connector
from pymongo import MongoClient
import csv

# MySQL Connection
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    database="migrasi",
    password="",
    )
mysqlCursor = mysql.cursor()

# MongoDB Connection
mongo = MongoClient("mongodb://localhost")
mongoCursor = mongo.csvmongo

# Migration Target (MySQL)
database = "migrasi"
table = "fandom"

url = "https://www.fandom.com/topics/movies"
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData)

ttl = re.findall(r'<div itemprop="name" class="card__title">(.*?)</div>', str(respData))
auth = re.findall(r'<span itemprop="name">(.*?)</span>', str(respData))

def normalize(text):
    text = text.replace("\\xe2\\x80\\x98", "'")
    text = text.replace("\\xe2\\x80\\x99", "'")
    text = text.replace("&amp;", "&")
    text = text.replace("&#039;", "'")
    text = text.replace("\\xe2\\x80\\x94", "-")
    text = text.replace("\\xc3\\xa9", "é")
    text = text.strip()
    
    return text
 
for i in range(len(ttl)):
    gettitle = normalize(ttl[i])
    getauth = normalize(auth[i])
     
    print(i)
    print("Title: ", gettitle)
    print("Author: ", getauth)
    print()
    
    query = 'INSERT INTO fandom (title, author) VALUES ("'+gettitle+'", "'+getauth+'")'
    print(query)
    
    mysqlCursor.execute(query)
    mysql.commit()
    
# Taking Data from MySQL
mysqlCursor.execute("USE {};".format(database))
mysqlCursor.execute("SELECT * FROM {};".format(table))

# Show SELECT result in Array
res = mysqlCursor.fetchall()
print(res)
print()
for row in res:
    data = []
    # print(row)
    for data_column in row:
        data.append(data_column)

    print(data)
    
    # Create MongoDB Format
    mongoFormat = {"article_id":data[0],
                   "title":data[1],
                   "author":data[2]}
    print(mongoFormat)
    print()
    
    # Insert data to MongoDB
    mongoCursor.fandom.insert_one(mongoFormat)