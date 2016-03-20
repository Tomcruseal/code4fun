#include<iostream>
#include<cmath>
#include <iomanip>
#include<ctime>
#include<stdio.h>
using namespace std;
clock_t start, finish;
long double computepi(int n);

int main() {
	int n;
	cin >> n;
	start = clock();
	cout << setprecision(63) <<computepi(n);
	finish = clock();
	double interval=finish - start;
	cout << "the time is :" << interval << endl;
	system("pause");
	return 0;
}
long double computepi(int n) {
	long double h = 1.0 / double(n);
	long double sum = 0;
//#pragma omp parallel for reduction(*:n)
	for (int i = 0;i<n;i++) {
		long double x = 0;
		x = h*(i + 0.5);
		sum += 4.0 / (1.0 + pow(x,2));
	}
	long double pi = h*sum;
		return pi;
}
