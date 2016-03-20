#include<iostream>
#include<list>
#include<string>
using namespace std;
string spliting(int i,int j,string s){
    string temp="";
    for(int counter=i;counter<j;counter++){
            temp.append(s,counter,1);
    }
    return temp;}

std::list<string> converting(string s){
	std::list<string> returning;
	for(int i=0;i<int(s.length());i++){
		string temp;
	    temp=s[i];
		returning.push_back(temp);}
	return returning;}

string deconverting(std::list<string> s){
	string returning;
	list<string>::iterator i;
	for (i=s.begin();i!=s.end();++i){
		returning.append(*i);}
	return returning;}

bool judgement(string ele,string **arrays ){
	int j=sizeof(arrays);
	for(int i=0;i<j;i++){
		string b=*arrays[i];
		if(b.compare(ele)==0){
			return 1;}}
	return 0;}

bool judgementb(string a,list<string> b){
	list<string>::iterator i;
	for(i=b.begin();i!=b.end();++i){
		if(a==*i){return 1;break;}}
	return 0;}
	

int judgementc(string a,list<string> b){
	list<string>::iterator i;
	int counts=0;
	for(i=b.begin();i!=b.end();++i){
		counts++;
		if(a==*i){return counts;break;}}
	;}

void compressionlz(string compString){
	int counter=0;
	int length=compString.length();
	std::list<string> saveDic;
	while(int(compString.length())>0){
		for(int a=0;a<int(compString.length());a++){
			std::list<string> temp=converting(spliting(0,a+1,compString));
			std::list<string> tempList=saveDic;
			if(judgementb(deconverting(temp),tempList)==0){
				saveDic.push_back(deconverting(temp));
				string temps=deconverting(temp);
				//cout<<"("<<counter<<","<<temps<<")"<<endl;
				cout<<"("<<judgementc(deconverting(temp),tempList)<<","<<temps[int(temps.length()) - 1]<<")"<<endl;
				counter+=1;
				length=compString.length();
				compString=spliting(a+1,length,compString);
				break;}}
		}
}

int main(){
	string test="inevermakeloveifuckveryhard";
	compressionlz(test);
	return 0;
}