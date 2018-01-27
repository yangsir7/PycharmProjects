#!/usr/bin/env python
#-*- coding=gbk -*-
import feedparser
import re

def getwords(html):
    # Remove all the HTML tags
    txt=re.compile(r'<[^>]+>').sub('',html)
    ss = re.compile(r'[…·/《》%\\\.\s+~\-～:。？！，：；‘’“”、0-9a-zA-Z]').sub('', txt)
    # Split words by all non-alpha characters
    # words=re.compile(r']]>').split(txt)
    words0=[]
    for s in ss:
        # print(s)
        words0.append(s)
    # words = re.compile(r'[^A-Z^a-z]+').split(txt)
    #  Convert to lowercase
    # return [word.lower( ) for word in words if word!='']
    return words0

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    d=feedparser.parse(url)
    wc={}
    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e: summary=e.summary
        else: summary=e.description
        # print(e.title)
        # print(e.summary)
        # Extract a list of words
        words=getwords(e.title+' '+summary)
        # print(words)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
    return d.feed.title,wc
# a,b=getwordcounts('http://news.baidu.com/n?cmd=1&class=civilnews&tn=rss&sub=0')
# print(a)

apcount={}
wordcounts={}
feedlist=[line for line in open('C:\\Users\\yangquan11\\Desktop\\feedlist.txt')]
for feedurl in feedlist:
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items( ):
        apcount.setdefault(word,0)
        if count>1:
            apcount[word]+=1

wordlist=[]
# for w,bc in wordcounts.items( ):
#     for s,d in bc.items():
#         frac=float(d)
#         if frac>2 and frac<5: wordlist.append(s)

for w,bc in apcount.items( ):
    frac=float(bc)/len(feedlist)
    # wordlist.append(w)
    if frac>0.3 and frac<0.5: wordlist.append(w)

out=open('C:\\Users\\yangquan11\\Desktop\\blogdata.txt','w')
out.write('Blog')
for word in wordlist:
    # print(word)
    out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items( ):
    out.write(blog)
    for word in wordlist:
        if word in wc: out.write('\t%d' % wc[word])
        else: out.write('\t0')
    out.write('\n')
out.close()
