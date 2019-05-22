#include <stdio.h>

int main(int argc, char *argv[]) {
    int N;
    char before[2001];
    char after[2001];

    while (~scanf("%d", &N)) {
        for (int i = 0; i < N; i++) {
            scanf(" %c", &before[i]);
        }

        int left = 0, right = N-1;
        int k = 0;

        while (left < right) {
            if (before[left] < before[right]) {
                after[k++] = before[left++];
            } else if (before[left] > before[right]) {
                after[k++] = before[right--];
            } else {
                // 两边相等
                int x = left + 1;
                int y = right - 1;

                while (x < y && before[x]==before[y]) {
                    x++;
                    y--;
                }

                if (before[x] < before[y]) {
                    after[k++] = before[left++];
                } else {
                    after[k++] = before[right--];
                }
            }
        }

        // 这两行可以通过更改 left <= right 省略
        after[N-1] = before[left];
        after[N] = '\0';

        int count = 0;
        for (int i = 0; i < N; i++) {
            printf("%c", after[i]);
            count++;

            if (count%80 == 0 && i < N-1) {
                printf("\n");
            }
        }
    }

    return 0;
}
