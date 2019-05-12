#include <stdio.h>

#define mod 10000

int quickpower(int n) {
    int ans = 1;
    int base = n % mod;  // 防止 int 表示不了
    int b = n;

    while (b) {
        if (b % 2 == 1) {
            ans = (ans * base) % mod;
        }

        base = (base * base) % mod;
        b /= 2;
    }

    return ans;
}

int main() {
    int T;

    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int num;
        scanf("%d", &num);
        int ans = quickpower(num)%10;
        printf("%d\n", ans);
    }

    return 0;
}