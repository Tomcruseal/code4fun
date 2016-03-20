#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import commands
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
http
'''
url1='http://202.38.193.235/jiaowuchu/%E9%A6%96%E9%A1%B5/%E6%95%99%E5%8A%A1%E9%80%9A%E7%9F%A51/more.aspx'
url2='http://202.38.193.235/jiaowuchu/%E9%A6%96%E9%A1%B5/%E5%AD%A6%E9%99%A2%E4%BF%A1%E6%81%AF/more.aspx'
headers1={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

try:
    req1=urllib2.Request(url=url1,headers=headers1)
    req2=urllib2.Request(url=url2,headers=headers1)
    response1=urllib2.urlopen(req1)
    response2=urllib2.urlopen(req2)
except:urllib2.URLError
    print 'connection error!'

getFile1=open("/home/kim/theTempHtmlFiles/responseFile1.html",'w')
getFile2=open("/home/kim/theTempHtmlFiles/responseFile2.html",'w')
htmlObtain1=response1.read()
htmlObtain2=response2.read()
htmlTrans1=htmlObtain1.decode('gb2312','ignore').encode('utf-8')
htmlTrans2=htmlObtain2.decode('gb2312','ignore').encode('utf-8')
getFile1.write(htmlTrans1)
getFile2.write(htmlTrans2)

time.sleep(0.5)
"""
Analysis
"""

myFile1=open("/home/kim/theTempHtmlFiles/responseFile1.html",'r')
myFile2=open("/home/kim/theTempHtmlFiles/responseFile2.html",'r')
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

targetFile=open("/home/kim/theTempHtmlFiles/targetFiles.html",'w')
targetFile.write(totalString)

(statusPre,outputPre)=commands.getstatusoutput("md5sum /home/kim/theTempHtmlFiles/targetFiles.html")
md5ValuePre=outputPre[0:32]
time.sleep(0.05)
print md5ValuePre
"""
this file is meant to send the html file to my email
via a stmp server
"""

mymsg=MIMEMultipart('related')
'''
attachment
'''
attachment=MIMEText(open('/home/kim/theTempHtmlFiles/targetFiles.html','rb').read(),'base64','utf-8')
attachment["Content-Type"]='application/octet-stream'

attachment["Content-Disposition"]='attachment;filename="Message.html"'
mymsg.attach(attachment)


mymsg['to']='xxxxxxxx@xxx.com'
mymsg['from']='xxxxxxxxx@xxx.com'
mymsg['subject']='Information'

'''
send email
'''
(statusCur,outputCur)=commands.getstatusoutput("md5sum /home/kim/theHtmlFiles/targetFiles.html")
md5ValueCur=outputCur[0:32]
print md5ValueCur
#if md5ValueCur!=md5ValuePre :
try:
    server=smtplib.SMTP()
    server.connect('xxxxxxx')
    server.login('xxxxxxxxx','xxxxxxxxx')
    server.sendmail(mymsg['from'],mymsg['to'],mymsg.as_string())
    server.quit()
    print 'Mission Success'
except Exception,e:
    print str(e)
#else:
    print "the website has not refresh yet"
