#include<iostream>
#include<stirngSplit.cpp>
#include<judgeenelementinaarray.cpp>
#include<stirng>
using namespace std;
string compressionlz(string compString){
	int counter=0;
	int length=compString.length();
	string saveDic={};
	while(compString.length()>0){
		for(int a=0;a<compString.length();a++){
			string temp=spliting(0,a+1)
			string tempList=saveDic;
			if(judgement(temp,tempList)==0){
				saveDic.append(temp);
				counter+=1;
				compString=spliting(a+1,length,compString);
				break;


