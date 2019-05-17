#include <stdio.h>

int main() {
    int n;

    while (~scanf("%d", &n) && n != 0) {
        int sum = 0;

        int a;
        for (int i = 0; i < n; i++) {
            scanf("%d", &a);
            sum += a;
        }

        printf("%d\n", sum);
    }

    return 0;
}