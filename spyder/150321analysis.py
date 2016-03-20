#coding:utf-8 
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


print 'This is anther html file'
myFile=open('./KuaiPan/codes/htmlFile2.html','r')
soup=BeautifulSoup(myFile)

getPoint=" "
tempList=soup.find_all("a")
for elements in tempList:
    
    getPoint+=(elements.next_element+'\n')
    
print getPoint

getPointFile=open("getPointFile.html",'w')
getPointFile.write(getPoint)



