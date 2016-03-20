#include<iostream>
using namespace std;
typedef int DataType;
typedef struct                        //the sequential list
{
	DataType data[1000];          //a large enough array
	int SeqLength;//the lenght of the sequentiallist
}SeqList;
SeqList *Initial();    //to initialize the sequential list
void Add(SeqList*L,int n);    //add elements to the sequential list form the keyboard one by one
void Delete(SeqList*L,int i);    //delete the ith element
int Insert(SeqList*L,int i,DataType inputElem);    //to insert element "inputElem" to the ith
void DisplayAll(SeqList*L);    //display the sequential list on the screen
int Find(SeqList*L,int x);    //search for x
int Insert(SeqList*L,int i,DataType inputElem)
{
	int j=0;
	for(j=L->SeqLength;j>=i;j--)
	{
		L->data[j+1]=L->data[j];
	}
	L->data[i]=inputElem;
	L->SeqLength++;
	return 1;
}
void DisplayAll(SeqList*L)
{
	cout<<"The elements are"<<endl;
	for(int i=0;i<L->SeqLength;i++)
	{
		cout<<L->data[i]<<" ";
	}
	cout<<endl;
}
void Delete(SeqList*L,int i)
{
	int j=0;
	for(j=i;j<L->SeqLength;j++)
	{
		L->data[j]=L->data[j+1];
	}
	L->SeqLength--;
	cout<<"the"<<i<<"th element deleted successfully!"<<endl;
}
SeqList *Initial()
{
	SeqList *L;
	L=new SeqList;
	L->SeqLength=0;
	return L;
}

void Add(SeqList*L,int n)
{
	cout<<"Please enter the elements!"<<endl;
	for(int i=0;i<n;i++)
	{
		cin>>L->data[i];
		L->SeqLength++;
	}
}
int Find(SeqList*L,int x)
{
	int i;
	for(i=0;i<L->SeqLength;i++)
	{
		if(L->data[i]==x)
		{
			return x;
			break;
		}
	}
	return -1;
}
