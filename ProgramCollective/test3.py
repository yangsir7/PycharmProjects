#!/usr/bin/env python
#-*- coding=cp936 -*-

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re
from ProgramCollective import nn
import jieba
import time
# jieba.add_word('·����')
# stopwords = ['��', '����', '��', '��']
# seg_list = jieba.cut("�����������廪��ѧ", cut_all=False)
# print([r for r in seg_list])
# print(stopwords)
def getminutes(t):
    x=time.strptime(t,'%H:%M')
    return x[3]*60+x[4]
# print(time.clock())
a=getminutes('01:00')
print(a)