#include <stdio.h>

int main() {
    int n;
    int a[5842] = {1};
    int t2 = 0;
    int t3 = 0;
    int t5 = 0;
    int t7 = 0;
    int temp, i;
	for(i = 1; i < 5842; i++) {
        // 找到 5842 个只能被 2 3 5 7 整除的数
		while(a[t2]*2 <= a[i-1])	t2++;
		while(a[t3]*3 <= a[i-1])	t3++;
		while(a[t5]*5 <= a[i-1])	t5++;
		while(a[t7]*7 <= a[i-1])	t7++;
		temp = a[t2]*2;
		if(a[t3]*3 < temp)	temp = a[t3]*3;
		if(a[t5]*5 < temp)	temp = a[t5]*5;
		if(a[t7]*7 < temp)	temp = a[t7]*7;
		a[i] = temp;
	}

	while(scanf("%d", &n) == 1 && n) {
		printf("The %d", n);
		if(n%10 == 1 && n%100 != 11)
			printf("st");
		else if(n%10 == 2 && n%100 != 12)
			printf("nd");
		else if(n%10 == 3 && n%100 != 13)
			printf("rd");
		else
			printf("th");
		printf(" humble number is %d.\n", a[n-1]);
	}

    return 0;
}