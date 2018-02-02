#!/usr/bin/env python
#-*- coding=utf-8 -*-

import ProgramCollective.chapter4.searchengine as searchengine

dirfile = 'C:\\Users\\yangquan1\\PycharmProjects\\ProgramCollective\\searchindex.db'
crawler= searchengine.crawler(dirfile)
# crawler.createindextables()
# pages= ['http://www.baidu.com/']
# crawler.crawl(pages)
# for row in crawler.con.execute('select * from wordlist'):
#     try:
#         print(row)
#     except:
#         print('eeee')

# crawler.calculatepagerank( )
#
e= searchengine.searcher(dirfile)
cur=crawler.con.execute('select * from pagerank order by score desc')
for i in range(3):
    a=cur.__next__()
    print(a,e.geturlname(a[0]))
r=e.query('体育')
# print(r[-1][1])
# w=e.con.execute("select word from wordlist where rowid= %d" % r[-1][1]).fetchone()
# print(w)
