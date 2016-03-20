#include<iostream>
#include<list>
#include<string>
#include<sstream>
using namespace std;

string get(int n,list<string> origional){
	list<string>::iterator iter=origional.begin();
	for(int ix=0;ix<n;++ix) ++iter;
	return *iter;
}

string decompressionlz(list<string> LList,string compressed){
	string decompressed;
	for(int i=0;i<int(compressed.length());i=i+2){
		string temp;
		string temps;
		temp=get(i,LList);
		string tempCompressed;
		stringstream stream;
		stream<<compressed[i+1];
		tempCompressed=stream.str();
		temps=temp.append(tempCompressed);
		decompressed.append(temps);}
	return decompressed;
}

int main(){
	list<string> testQi;
	testQi.push_back("a");
	testQi.push_back("ab");
	testQi.push_back("f");
	testQi.push_back("fc");
	testQi.push_back("k");
	string testone="0a0b1i";
	string result=decompressionlz(testQi,testone);
	cout<<result;
	return 0;
}

