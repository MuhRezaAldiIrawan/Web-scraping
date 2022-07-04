import csv
from email.quoprimime import quote
from venv import create
from pymongo import MongoClient


#Koneksi MongoDb
mongo = MongoClient('mongodb://127.0.0.1:27017')
mongoCursor = mongo.csvMongo


with open('iris.csv', newline='') as csvfile:
    #baca file csv
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #next(reader)
    
    #print(reader)
    #jabarkan tiap row
    for row in reader:
        panjang_daun = row[0]
        lebar_daun = row[1]
        panjang_bunga = row[2]
        lebar_bunga = row[3]
        jenis_bunga = row[4]
        
        mongoFormat = {"panjang_daun": panjang_daun,
                       "lebar_daun": lebar_daun,
                       "panjang_bunga": panjang_bunga,
                       "lebar_bunga": lebar_bunga,
                       "jenis_bunga": jenis_bunga}
        
        #print(mongoFormat)
        
        mongoCursor.irish.insert_one(mongoFormat)
        
        
        
         