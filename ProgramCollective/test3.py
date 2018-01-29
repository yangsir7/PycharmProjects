#!/usr/bin/env python
#-*- coding=cp936 -*-

import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re
from ProgramCollective import nn
import jieba
jieba.add_word('路明非')
stopwords = ['的', '包括', '等', '是']
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print([r for r in seg_list])
print(stopwords)