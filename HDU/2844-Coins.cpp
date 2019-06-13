// 分类：多重部分和问题，多重背包，二进制优化，优先队列

#include <stdio.h>
#include <string.h>

int n, m;
int V[105];
int C[105];

/* 超时
bool isSatisfied(int index, int cost) {
    if (cost < 0) {
        return false;
    }

    if (cost == 0) {
        return true;
    }

    if (index == n+1) {
        return false;
    }

    bool flag = false;
    for (int i = 0; i <= C[index]; i++) {
        flag = flag || isSatisfied(index+1, cost-i*V[index]);

        if (flag) {
            break;
        }
    }

    return flag;
}
*/

int dp[100010];

int maxab(int i, int j) {
    return i > j ? i : j;
}

void CompletePack(int v, int w, int m) {
    for (int j = v; j <= m; j++) {
        dp[j] = maxab(dp[j], dp[j-v]+w);
    }
}

void ZeroOnePack(int v, int w, int m) {
    for (int j = m; j >= v;j--) {
        dp[j] = maxab(dp[j], dp[j-v]+w);
    }
}

void MultiPack(int v, int w, int m, int c) {
    if (v*c > m) {
        CompletePack(v, w, m);
    } else {
        int k = 1;
        while (k < c) {
            ZeroOnePack(k*v, k*w, m);
            c -= k;
            k *= 2;
        }
        ZeroOnePack(c*v, c*w, m);
    }
}

int main(int argc, char *argv[]) {
    while (~scanf("%d%d", &n, &m)) {
        if (n == 0 && m == 0) {
            break;
        }

        for (int i = 1; i <= n; i++) {
            scanf("%d", &V[i]);
        }

        for (int i = 1; i <= n; i++) {
            scanf("%d", &C[i]);
        }

        /*
        int count = 0;
        for (int i = 1; i <= m; i++) {
            if (isSatisfied(0, i)) {
                count++;
            }
        }
        */

        memset(dp,0,sizeof(dp));
        for (int i = 1; i <= n; i++) {
            MultiPack(V[i], V[i], m, C[i]);
        }

        int sum = 0;
        for (int i = 1; i <= m; i++) {
            if (dp[i] == i) {
                sum++;
            }
        }

        printf("%d\n", sum);
    }

    return 0;
}
