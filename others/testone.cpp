#include<iostream>
#include"xiaomaHW.h"
using namespace std;
int main()
{
	SeqList *L;
	L=Initial();
	Add(L,5);
	Insert(L,3,9);
	DisplayAll(L);
	Delete(L,2);
	DisplayAll(L);
	return 0;
}


	
