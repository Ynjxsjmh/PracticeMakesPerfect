#include <stdio.h>

int main(){
    int cases;

    scanf("%d", &cases);

    int n[10001];

    for (int k = 0; k < cases; k++) {
        int count;
        int biggest = 0;
        int flag = 1;
        scanf("%d", &count);

        for (int i = 0; i < count; i++) {
            scanf("%d", &n[i]);
            if (n[i] > biggest) {
                biggest = n[i];
            }
        }

        int i;
        int j;
        for (i = biggest; flag; i += biggest) {
            for (j = 0; j < count; j++) {
                if (i % n[j] != 0) {
                    // i 就是可能的最大公因数
                    break;
                }
            }

            if (j == count) {
                // 找到最大公因数，结束循环
                printf("%d\n", i);
                flag = 0;
            }
        }
    }

    return 0;
}