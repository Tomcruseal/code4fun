import os
import time
counter=0
while True:
    try:
        os.sys('python /home/kim/codes/150322final.py')
        counter+=1
        print 'application runs for'+str(counter)+'times'
        time.sleep(5)
    except:
        print 'error occurred'
