# -*- coding: utf-8 -*-
from ftplib import FTP
ftp=FTP()
'''def download(filename):
	f=open(filename,'wb')
	filenameLocal='RETR' + filename
	ftp.retrbinary(filenameLocal,f.write)'''
	
def upload():
		f=open('F:/CN_20151222.txt','rb')
		#filenameServer='STOR' + 'CN_20151222.txt'
		ftp.storbinary('STOR /CN_20151222',f)
		f.close()