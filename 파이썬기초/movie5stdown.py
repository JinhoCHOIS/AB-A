#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import time
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'

page = urlopen(url)
soup = BeautifulSoup(page,"html.parser")

divList = soup.find_all('div', attrs={"class":"tit3"})
a=[];b=[];c=[];d=[];e=[];f=[];g=[]

for i in range(5):
    a.append(divList[i].find('a').get('href'))
    b.append(a[i].split('='))
    c.append(b[i][1])
    d.append('https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='+c[i])
    e.append(urlopen(d[i]))
    f.append(BeautifulSoup(e[i],"html.parser"))
    g.append(f[i].find('img').get('src'))
    
while 1:
    for j in range(5) :
        urlretrieve(g[j], "./movie%d.jpg" %(j+1))
        time.sleep(2)        

