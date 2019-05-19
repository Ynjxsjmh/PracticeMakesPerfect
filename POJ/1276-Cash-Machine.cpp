#include <stdio.h>
#include <string.h>

#define Max(a, b) a > b ? a : b

int dp[100001], cost[11], count[11], cash;

void ZeroOnePack(int cost) {
    for (int i = cash; i >= cost; i--) {
        dp[i] = Max(dp[i], dp[i-cost]+cost);
    }
}

void CompletePack(int cost) {
    for (int i = cost; i <= cash; i++) {
        dp[i] = Max(dp[i], dp[i-cost]+cost);
    }
}

void MultiplePack(int cost, int count) {
    if (cost * count > cash) {
        CompletePack(cost);
    } else {
        int k = 1;
        while (k < count) {
            ZeroOnePack(k*cost);
            count -= k;
            k *= 2;
        }
        ZeroOnePack(count*cost);
    }
}


int main(int argc, char *argv[]) {
    int n;

    while(~scanf("%d%d", &cash, &n)) {
        for (int i = 1; i <= n; i++) {
            scanf("%d%d", &count[i], &cost[i]);
        }

        memset(dp, 0, sizeof(dp));

        for (int i = 1; i <= n; i++) {
            MultiplePack(cost[i], count[i]);
        }

        printf("%d\n", dp[cash]);
    }

    return 0;
}
