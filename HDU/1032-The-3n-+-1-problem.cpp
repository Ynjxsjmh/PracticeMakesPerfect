#include <stdio.h>

int count(int n) {
    int ans = 1;

    while (n != 1) {
        if (n % 2 == 1) {
            n = 3*n+1;
        } else {
            n = n/2;
        }
        ans++;
    }

    return ans;
}

int main() {
    int a, b;

    while (~scanf("%d%d", &a, &b)) {
        printf("%d %d ", a, b);

        int temp;
        if (a > b) {  // 保证 a小b大
            temp = b;
            b = a;
            a = temp;
        }

        int biggest = count(a);

        for (int i = a; i <= b; i++) {
            if (count(i) > biggest) {
                biggest = count(i);
            }
        }

        printf("%d\n", biggest);
    }

    return 0;
}