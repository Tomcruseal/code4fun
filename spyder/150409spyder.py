#coding:utf-8
import re
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import time
#global contents
localSavePath='E:\\Python27\\yellow\\'

def downLoad(urls):
    headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
              (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    req1=urllib2.Request(url=urls,headers=headers1)
    content=urllib2.urlopen(req1).read()
    pattern='[0-9]*\.jpg'  #match for a string of numbers
    match=re.search(pattern,urls)
    if match:
        print 'Downloading',match.group()
        filename=localSavePath+match.group()
        print filename
        temp=open(filename,'wb')
        temp.write(content)
        temp.close()
    else:
        print 'None'

def analysis(htmlUrl):
    headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
              (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    req2=urllib2.Request(url=htmlUrl,headers=headers1)
    global contents
    try:
        res=urllib2.urlopen(req2)
        contents=res.read()
    except:
        print 'error'
    htmlfile=open("E:\\Python27\\blue\\tempFile.html",'wb')
    htmlfile.write(contents)
    htmlfile.close()

def findTheImage(filename):
    targetfile=open('E:\\Python27\\blue\\tempFile.html','rb')
    soup=BeautifulSoup(targetfile)
    tempList=soup.find_all("img",id="bigImg")
    tempList2=soup.find_all("a",class_="next")
    print tempList2
    if tempList:
        for i in tempList:
            obtainUrl=i.get('src')
            print obtainUrl
            downLoad(obtainUrl)
    if tempList2:
        for j in tempList2:
            obtainUrls='http://desk.zol.com.cn'+j.get('href')
            print 'sb',obtainUrls
            analysis(obtainUrls)
    else:
        print 'no picture bo JB!'


'''
fire the hole!!!
'''
theUrl='http://desk.zol.com.cn/bizhi/5296_65526_2.html'
analysis(theUrl)
findTheImage('E:\\Python27\\blue\\tempFile.html')
