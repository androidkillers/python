# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url ='http://www.mzitu.com/zipai/'
start_html = requests.get(all_url,headers=headers)
Soup = BeautifulSoup(start_html.text,'lxml')
#print(Soup)
imgs = Soup.find_all('img')
for img in imgs:
    img_url = img['src']
    name = img_url[-9:-4]
    Img = requests.get(img_url,headers=headers)
    f = open(name+'.jpg','ab')
    f.write(Img.content)
    f.close()
