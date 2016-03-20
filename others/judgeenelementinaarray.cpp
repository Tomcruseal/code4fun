#include<string>
using namespace std;
bool judgement(string ele,*string array ){
	int j=*array.length();
	for(int i=0;i<j;i++){
		if(ele==*array[i]){
			return 1;}}
	return 0;}	
