#include <stdio.h>

int main() {
    int N;

    while (~scanf("%d", &N)) {
        int sum = 0;
        int a;
        for (int i = 0; i < N; i++) {
            scanf("%d", &a);
            sum += a;
        }

        printf("%d\n", sum);
    }

    return 0;
}