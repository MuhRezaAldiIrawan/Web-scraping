from asyncore import write
import csv
from email.quoprimime import quote
from venv import create
from pymongo import MongoClient


#Koneksi MongoDb
mongo = MongoClient('mongodb://127.0.0.1:27017')
mongoCursor = mongo.csvMongo


with open('Mongo_iris.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
    #cari data dari Mongo
    hasil = mongoCursor.irish.find()
   
    
    #Jabarkan data dari mongo
    writer.writerow({'panjang_daun','lebar_daun','panjang_bunga','lebar_bunga','jenis_bunga'})
    for doc in hasil:
        panjang_daun = doc["panjang_daun"]
        lebar_daun = doc["lebar_daun"]
        panjang_bunga = doc["panjang_bunga"]
        lebar_bunga = doc["lebar_bunga"]
        jenis_bunga = doc["jenis_bunga"]
        
        writer.writerow({panjang_daun,lebar_daun,panjang_bunga,lebar_bunga,jenis_bunga})
        
    
    
 
   