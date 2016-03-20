#include "omp.h"
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
short nums[900000000];

int main() {
	srand(time(NULL));
	int cnt[4][16] = { 0 };
	int cnt2[16] = { 0 };
	int cnt3[16] = { 0 };
	//int num,n=0;
	//freopen("./input.txt", "r", stdin);
	//while (scanf("%d", &num) != EOF)
	//	nums[n++] = num;
	int i,j,n=900000000;

	for (i = 0; i < n; i++) {
		nums[i] = rand() % 16;
	}

	int a = n / 4;

	double d2 = omp_get_wtime();
#pragma omp parallel for
	for (j = 0; j < 4; j++) {
		int *c = cnt[j];
		int st = j*a, en = (j + 1)*a;
		short *nn = nums + j*a;
		for (i = 0; i < a; i++) {
			++c[*(nn++)];
		}


	}

	for (i = 0; i < 16; i++) {
		for (int j = 0; j < 4; j++) {
			cnt2[i] += cnt[j][i];
		}
	}

	for (i = a * 4; i < n; i++) {
		++cnt2[nums[i]];
	}

	d2 = omp_get_wtime() - d2;

	

	for (i = 0; i < 16; i++) {
		printf("%d", cnt2[i]);
		printf("%c", (i == 15 ? '\n':' '));
	}
	printf("parallel time: %.6lfs\n", d2);

	short *nnn = nums;
	double d1 = omp_get_wtime();
	for (i = 0; i < n; i++)
		++cnt3[*(nnn++)];
	d1 = omp_get_wtime() - d1;
	for (i = 0; i < 16; i++) {
		printf("%d", cnt3[i]);
		printf("%c", (i == 15 ? '\n' : ' '));
	}


	printf("sequencial time: %.6lfs\n", d1);
	system("pause");
	return 0;

}