#include <cstdio>
#include <cstring>
#include <algorithm>

int a[1001];

int main() {
    int cases, n;

    scanf("%d", &cases);

    for (int i = 0; i < cases; i++) {
        scanf("%d", &n);

        memset(a, 0, sizeof(a));

        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }

        std::sort(a, a+n);;

        for (int i = 0; i < n; i++) {
            if (i != n-1) {
                printf("%d ", a[i]);
            } else {
                printf("%d\n", a[i]);
            }
        }
    }

    return 0;
}