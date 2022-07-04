import urllib.request
import bs4
from bs4 import BeautifulSoup
import re


url = 'https://www.sinjaikab.go.id/v4/'

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
    

