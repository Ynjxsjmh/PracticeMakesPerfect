// 分类：背包问题

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int value[1005];
int volume[1005];
int dp[1005][1005];
int T, N, V;

// 第i个bone挑选体积小于j的
int rec(int i, int j) {
    if (dp[i][j] >= 0) {
        return dp[i][j];
    }

    int res;
    if (i == N) {
        res = 0;
    } else if (volume[i] > j) {
        res = rec(i+1, j);
    } else {
        res = max(rec(i+1, j), rec(i+1, j-volume[i])+value[i]);
    }

    dp[i][j] = res;

    return res;
}

int main(int argc, char *argv[]) {
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf("%d%d", &N, &V);
        memset(value, 0, sizeof(value));
        memset(volume, 0, sizeof(volume));
        memset(dp, -1, sizeof(dp));

        for (int i = 0; i < N; i++) {
            scanf("%d", &value[i]);
        }

        for (int i = 0; i < N; i++) {
            scanf("%d", &volume[i]);
        }

        printf("%d\n", rec(0, V));
    }

    return 0;
}
