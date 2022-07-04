from msilib.schema import tables
import mysql.connector
from pymongo import MongoClient

#Koneksi MysqlDb
mysql = mysql.connector.connect(host='localhost', password='', user='root')
mysqlCursor = mysql.cursor() 



#Koneksi MongoDb
mongo = MongoClient('mongodb://127.0.0.1:27017')
mongoCursor = mongo.migrasi

#Target Koneksi
database = 'tokopedia'
table = 'toko'

#Ambil Data dari Mysql
mysqlCursor.execute('USE {};'.format(database))
mysqlCursor.execute('SELECT * FROM {};'.format(table))

#Uraikan hasil select dalam bentuk array
hasil = mysqlCursor.fetchall()


print(hasil)
for row in hasil:
    data = []
    #print(row)
    for data_column in row:
        data.append(data_column)
        
    print(data)
    
    mongoFormat = {"id_toko": data[0],
                   "nama_toko": data[1],
                   "kategori": data[2]}
    print(mongoFormat)
    print()
    
    #Masukan Data Kedalam Mongodb
    mongoCursor.toko.insert_one(mongoFormat)
        
         