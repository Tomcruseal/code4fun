theString='inevermakeloveifuckveryhard'
def compressionlz(compString):
    counter=0
    saveDic={}
    while(len(compString)>0):
        for a in range(0,len(compString)):
            temp=compString[:a+1]
            tempList=list(saveDic.values())
            if temp not in tempList:
                counter+=1
                tempDict={counter:temp}
                saveDic.update(tempDict)
                compString=compString[(a+1):]
                break
    print saveDic      

compressionlz(theString)            
