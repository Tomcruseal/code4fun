#coding:utf-8
'''import sys
reload(sys)
sys.setdefaultencoding('utf-8')'''
import urllib2

url1='http://202.38.193.235/jiaowuchu/'
url2='http://202.38.193.235/jiaowuchu/%E9%A6%96%E9%A1%B5/%E6%95%99%E5%8A%A1%E9%80%9A%E7%9F%A51/more.aspx'
headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
req=urllib2.Request(url=url1,headers=headers1)
response=urllib2.urlopen(req)
#print response.read()
getFile=open("htmlFile.html",'w')
htmlGet=response.read()
htmlTrans=htmlGet.decode('gb2312','ignore').encode('utf-8')
getFile.write(htmlTrans)
#getFile.close()

'''
another html file
'''
req2=urllib2.Request(url=url2,headers=headers1)
response2=urllib2.urlopen(req2)
getFile2=open("htmlFile2.html",'w')
htmlGet2=response2.read()
htmlTrans2=htmlGet2.decode('gb2312','ignore').encode('utf-8')
getFile2.write(htmlTrans2)
