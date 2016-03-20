#coding:utf-8
'''
this file is meant to invoking scs-sdk
to make connection with the cloud storage
'''
import sinastorage
from sinastorage.bucket import SCSBucket
sinastorage.setDefaultAppInfo('XXXXXXXXXXXXXXXXXXXXXXXX','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
s=SCSBucket('mystorage',secure=True)
#print s
#s.putFile('mystorage','D:\\a.jpg')   test

s.putFile('math1','D:\\Mathematical Modeling\\math1.rar')
