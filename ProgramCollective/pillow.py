#!/usr/bin/env python
#-*- coding=cp936 -*-

import searchengine
from sqlite3 import dbapi2 as sqlite

crawler=searchengine.crawler('C:\\Users\\yangquan11\\PycharmProjects\\untitled\\searchindex.db')
# crawler.createindextables( )
# pages= ['http://www.baidu.com/']
# crawler.crawl(pages)
# for row in crawler.con.execute('select * from link'):
#     try:
#         print(row)
#     except:
#         print('eeee')
#
# crawler.calculatepagerank( )
#
e=searchengine.searcher('C:\\Users\\yangquan11\\PycharmProjects\\untitled\\searchindex.db')
# cur=crawler.con.execute('select * from pagerank order by score desc')
# for i in range(3):
#     a=cur.__next__()
#     print(a,e.geturlname(a[0]))
r=e.query('百 度 一 下')
# print(r[-1][1])
# w=e.con.execute("select word from wordlist where rowid= %d" % r[-1][1]).fetchone()
# print(w)
