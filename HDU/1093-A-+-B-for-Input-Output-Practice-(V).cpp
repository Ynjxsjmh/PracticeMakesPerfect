#include <stdio.h>

int main() {
    int N, M;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &M);
        int sum = 0;
        int a;

        for (int j = 0; j < M; j++) {
            scanf("%d", &a);

            sum += a;
        }

        printf("%d\n", sum);
    }

    return 0;
}