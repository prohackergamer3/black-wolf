from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
import sys
while True:
 sonuclar = {}
 query = input("Ara:")
 try:
     for i in search(query):
                try:
                    title = urlopen(i)
                    html = BeautifulSoup(title,"html.parser")
                    print(html.title.string)
                    sonuclar[html.title.string] = i
                    sec = input("seçin:")
                    webbrowser.open(sonuclar[sec])
                    break
                except:
                    print("HATA")
                    sys.exit()
            
 except:
     print("HATA")
     pass    
        
    