'''import os
m=os.popen("md5sum ./Downloads/Message.html")
print m
print os.system("md5sum ./Downloads/3.java")'''
import commands
(status,output)=commands.getstatusoutput("md5sum ./Downloads/Message.html")
print status
print output
print output[0:32]
md5Value=output[0:32]
