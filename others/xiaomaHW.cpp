#include<iostream>
using namespace std;
typedef int DataType;
typedef struct
{
	DataType data[1000];
	int SeqLength;//the lenght of the sequentiallist
}SeqList;
SeqList *Initial();
void Add(SeqList*L,int n);
int Delete(SeqList*L,int i);
int Insert(SeqList*L,int i,DataType inputElem);
void DisplayAll(SeqList*L);
int Insert(SeqList*L,int i,DataType inputElem)
{
	for(j=L->SeqLength;j>=i;j--)
	{
		L->data[j+1]=L->data[j];
	}
	L->data[i]=inputElem;
	L->SeqLength++;
	return 1;
}
