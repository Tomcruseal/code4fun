#coding:utf-8
"""
this file is meant to send the html file to my email
via a stmp server
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
mymsg=MIMEMultipart('related')
'''
attachment
'''
attachment=MIMEText(open('./targetFile.html','rb').read(),'base64','utf-8')
attachment["Content-Type"]='application/octet-stream'
#attachment.add_header('Content-Disposition','attachment',filename=('utf-8','','Message.html')
#attachment['Content-Disposition']='attachment;filename=('utf-8','','Message.html')'
attachment["Content-Disposition"]='attachment;filename="Message.html"'
mymsg.attach(attachment)


mymsg['from']='XXXXXXXXXXXX@xx.com'
mymsg['subject']='Information'
                      
'''
send email
'''
try:
    server=smtplib.SMTP()
    server.connect('smtp.xx.com')
    server.login('xxxxxxxx','xxxxxxxxxx')
    server.sendmail(mymsg['from'],mymsg['to'],mymsg.as_string())
    server.quit()
    print 'Mission Success'
except Exception,e:
    print str(e)                  



                      
                      
                      
                      
