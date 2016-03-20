theString='inevermakeloveifuckveryhard'
def compressionlz(compString):
    #a=0
    
    counter=0
    saveDic={}
    temper={counter:compString[0]}
    saveDic.update(temper)
    print (counter,compString[0])
    compString=compString[1:]
    print compString
    while(len(compString)>0):
        
        for a in range(0,len(compString)-1):
            #temp=compString[:a+1]
            #tempList=list(saveDic.values())
            #print tempList,compString
            if temp not in tempList:
                print "the temp is" +temp
                counter+=1
                tempDict={counter:temp}
                print tempDict
                saveDic.update(tempDict)
                compString=compString[(a+1):]
                print compString
            else:
                temp=compString[:a+1]
                tempList=list(saveDic.values())
    print saveDic          
compressionlz(theString)

                
        
