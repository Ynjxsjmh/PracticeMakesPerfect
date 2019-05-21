#include <stdio.h>
#include <string.h>

int Min(int a, int b) {
    return a < b ? a : b;
}

int main(int argc, char *argv[]) {
    int coin_num[4];
    int coin_cost_num[4];
    int value[4] = {5, 10, 20, 50};
    int sum;

    memset(coin_num, 0, sizeof(coin_num));

    while (~scanf("%d%d%d%d%d", &coin_num[0], &coin_num[1], &coin_num[2], &coin_num[3], &sum)) {
        int all = 0;
        memset(coin_cost_num, 0, sizeof(coin_cost_num));

        for (int i = 3; i >= 0; i--) {
            coin_cost_num[i] = Min(coin_num[i], sum/value[i]);
            sum -= coin_cost_num[i] * value[i];
            all += coin_cost_num[i];
        }

        if (sum > 0) {
            printf("-1\n");
        } else {
            for (int i = 0; i < 4; i++) {
                printf("%d ", coin_cost_num[i]);
            }
            printf("%d\n", all);
        }
    }

    return 0;
}

