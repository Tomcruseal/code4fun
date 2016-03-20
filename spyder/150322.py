#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url1='http://202.38.193.235/jiaowuchu/%E9%A6%96%E9%A1%B5/%E6%95%99%E5%8A%A1%E9%80%9A%E7%9F%A51/more.aspx'
url2='http://202.38.193.235/jiaowuchu/%E9%A6%96%E9%A1%B5/%E5%AD%A6%E9%99%A2%E4%BF%A1%E6%81%AF/more.aspx'
headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
          
req1=urllib2.Request(url=url1,headers=headers1)
req2=urllib2.Request(url=url2,headers=headers1)
response1=urllib2.urlopen(req1)
response2=urllib2.urlopen(req2)
getFile1=open("responseFile1.html",'w')
getFile2=open("responseFile2.html",'w')
htmlObtain1=response1.read()
htmlObtain2=response2.read()
htmlTrans1=htmlObtain1.decode('gb2312','ignore').encode('utf-8')
htmlTrans2=htmlObtain2.decode('gb2312','ignore').encode('utf-8')
getFile1.write(htmlTrans1)
getFile2.write(htmlTrans2)

time.sleep(0.005)
"""
Analysis
"""

myFile1=open("responseFile1.html",'r')
myFile2=open("responseFile2.html",'r')
soup1=BeautifulSoup(myFile1)
soup2=BeautifulSoup(myFile2)
tempList1=soup1.find_all("a")
tempList2=soup2.find_all("a")
totalString=" "
for elements in tempList1:
    totalString+=(elements.next_element+'\n')

totalString+="School Information Belows\n"    
for elements in tempList2:
    totalString+=(elements.next_element+'\n')

targetFile=open("targetFile.html",'w')
targetFile.write(totalString)
    


        
        

