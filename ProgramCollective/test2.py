#!/usr/bin/env python
#-*- coding=cp936 -*-

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re

def gettextonly(soup):
    v = soup.string
    if v == None:
        c = soup.contents
        resulttext = ''
        for t in c:
            subtext = gettextonly(t)
            resulttext += subtext + '\n'
        return resulttext
    else:
        return v.strip()

page= 'http://www.baidu.com/'
try:
    c = urllib.request.urlopen(page)
except:
    print("Could not open %s" % page)
soup = BeautifulSoup(c.read(),"lxml")
links = soup('a')
for link in links:
    if ('href' in dict(link.attrs)):
        url = urljoin(page, link['href'])
        if url.find("'") != -1: continue
        url = url.split('#')[0]  # remove location portion
        linkText = gettextonly(link)
        print(linkText)
