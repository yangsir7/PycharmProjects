#!/usr/bin/env python
#-*- coding=cp936 -*-

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re
from ProgramCollective import nn
page='C:\\Users\\yangquan11\\PycharmProjects\\untitled\\nn.db'
wordids=[1,2,3,4,5]
hiddenids=[1,2,3,4]
urlids=[0,2,1]

# node outputs
ai = [1.0]*len(wordids)
ah = [1.0]*len(hiddenids)
ao = [1.0]*len(urlids)
# create weights matrix
wi = [[hiddenid+wordid for hiddenid in hiddenids] for wordid in wordids]
wo = [[urlid+hiddenid for urlid in urlids] for hiddenid in hiddenids]
print(wi)
print('######')
print(wo)


mynet=nn.searchnet(page)
mynet.maketables( )
wWorld,wRiver,wBank =101,102,103
uWorldBank,uRiver,uEarth =201,202,203
mynet.generatehiddennode([wWorld,wBank],[uWorldBank,uRiver,uEarth])
for c in mynet.con.execute('select * from wordhidden'): print(c)
for c in mynet.con.execute('select * from hiddenurl'): print(c)
mynet=nn.searchnet(page)
mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])