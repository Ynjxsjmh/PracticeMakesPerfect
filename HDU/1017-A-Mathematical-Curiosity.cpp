#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);

    for (int i = 1; i <= num; i++) {
        int m, n;
        int x = 1;
        while (~scanf("%d%d", &n, &m)) {
            if (m == 0 && n == 0) {
                break;
            }

            int count = 0;
            for (int a = 1; a < n-1; a++) {
                for (int b = a+1; b < n; b++) {
                    if ( (a*a+b*b+m)%(a*b) == 0) {
                        count++;
                    }
                }
            }

            printf("Case %d: %d\n", x++, count);
        }
        if (i != num) {
            printf("\n");
        }
   }

    return 0;
}