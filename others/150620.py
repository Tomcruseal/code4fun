#coding:utf-8
import urllib2
import os,sys,time
url1='http://githubchina.sinaapp.com'
headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
while True:
        urllib2.Request(url=url1,headers=headers1)
	time.sleep(1)
