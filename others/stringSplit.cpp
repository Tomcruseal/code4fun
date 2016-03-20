#include<iostream>
#include<string>
#include<string.h>
using namespace std;
using std::string;

string spliting(int i,int j,string s){
    string temp="";
    for(int counter=i;counter<j;counter++){
            temp.append(s,counter,1);
    }
    return temp;}
int main(){
    string tests="abcdefghijk";
    string x=spliting(2,8,tests);
    cout<<x<<endl;
    return 0;}
