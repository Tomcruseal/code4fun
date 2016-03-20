# -*- coding: utf-8 -*-
from ftplib import FTP
import ftp_functions
import time
import sys
ftp=FTP()
timeout=30
port=21
ftp.connect('192.168.1.102',port,timeout)
ftp.login('XXXXXX','XXXXXXXXXX')
print ftp.getwelcome()
list=ftp.nlst()
for name in list:
	tempName=unicode(name,'UTF-8')
	print tempName

#print 'Please input the file you want to download'
print 'uploading--'
time.sleep(1)
f=open('F:/CN_20151222.txt','rb')
ftp.storbinary('STOR /CN_20151222',f)
f.close()
print "upload success!" 

time.sleep(1)
print 'Then download certain file'
print 'downloading--'
time.sleep(1)
fp=open('F:/password.txt','wb')
ftp.retrbinary('RETR /password.txt',fp.write)
fp.close()
print "download success"

'''def ftp_functionsdownload(filename):
	f=open(filename,'wb')
	filenameLocal='RETR' + filename
	ftp.retrbinary(filenameLocal,f.write)'''

'''def upload(filename):
	f=open(filename,'rb')
	filenameServer='STOR' + filename
	ftp.storbinary(filenameServer,f.write)'''	
	
		
