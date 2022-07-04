from msilib.schema import tables
import mysql.connector
from pymongo import MongoClient

#Koneksi MysqlDb
mysql = mysql.connector.connect(host='localhost', password='', user='root', database = 'tokopedia')
mysqlCursor = mysql.cursor() 

#Koneksi MongoDb
mongo = MongoClient('mongodb://127.0.0.1:27017')
mongoCursor = mongo.migrasi

#Ambil data dari MongoDb
hasil = mongoCursor.toko.find()

#Uraikan hasil MongoDb
for doc in hasil: 
    nama_toko = doc["nama_toko"]
    kategori = doc["kategori"]
    #kategori = str(doc["kategori"])  #jika bentuk integer
    
    query = "INSERT INTO toko(nama_toko,kategori) VALUES('"+nama_toko+"', '"+kategori+"')"
    #jika data bentuk integer maka hanya "+kategori+"
    
    print(query)
    
    mysqlCursor.execute(query)
    mysql.commit()
    




         