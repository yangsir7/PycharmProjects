#!/usr/bin/env python
#-*- coding=cp936 -*-
import time
import random
import math
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re
from ProgramCollective import nn
from ProgramCollective import optimization
import jieba
import time
# jieba.add_word('路明非')
# stopwords = ['的', '包括', '等', '是']
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print([r for r in seg_list])
# print(stopwords)
# s=[1,4,3,2,7,3,6,3,2,4,5,3]
domain=[(0,9)]*(len(optimization.people)*2)
# s=optimization.randomoptimize(domain,optimization.schedulecost)
# sc=optimization.schedulecost(s)
# s=optimization.hillclimb(domain,optimization.schedulecost)
# sc=optimization.schedulecost(s)
# s=optimization.annealingoptimize(domain,optimization.schedulecost)
# sc=optimization.schedulecost(s)
# s=optimization.geneticoptimize(domain,optimization.schedulecost)
# optimization.printschedule(s)
# sc=optimization.schedulecost(s)
# print(s)
# print(sc)

from ProgramCollective import dorm
dorm.printsolution([0,0,0,0,0,0,0,0,0,0])
s=optimization.randomoptimize(dorm.domain,dorm.dormcost)
dorm.dormcost(s)
optimization.geneticoptimize(dorm.domain,dorm.dormcost)
dorm.printsolution(s)
# pop=[]
# for i in range(50):
#     vec=[random.randint(0,9) for i in range(len(domain))]
#     print(i,'\t',vec)
#     pop.append(vec)