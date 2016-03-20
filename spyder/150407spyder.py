#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import sys
urls='http://www.sciencelzb.info'
headerse={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
req=urllib2.Request(url=urls,headers=headerse)
res=urllib2.urlopen(req)
getFile=open('fileReceived.html','w')
theAnswer=res.read()
getFile.write(theAnswer)
