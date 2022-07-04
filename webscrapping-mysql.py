import urllib.request
from msilib.schema import tables
import mysql.connector
import bs4
from bs4 import BeautifulSoup
import re


url = 'https://www.sinjaikab.go.id/v4/'

#Koneksi MysqlDb
mysql = mysql.connector.connect(host='localhost', password='', user='root', database = 'webscrapping')
mysqlCursor = mysql.cursor() 

req = urllib.request.Request(url)
respon = urllib.request.urlopen(req)
responData = respon.read()

#print(responData)

judul = re.findall(r'<div class="td-excerpt">(.*?)</div>', str(responData))

def normalisasi(text):
    text = text.replace("\\n", " ")
    text = text.replace("\\r", " ")
    text = text.strip()
    
    return text
    
for i in range(len(judul)): 
    getJudul = normalisasi(judul[i])
    print(i)
    print(getJudul)
    print()
    
query = "INSERT INTO body(isi) VALUES('"+isi+"')"
    #jika data bentuk integer maka hanya "+kategori+"
    
print(query)
    
mysqlCursor.execute(query)
mysql.commit()
