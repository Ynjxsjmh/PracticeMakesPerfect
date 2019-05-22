#include <cstdio>
#include <algorithm>

int main(int argc, char *argv[]) {
    int R, n;
    int troops[1001];

    while (~scanf("%d%d", &R, &n)) {
        if (R == -1 && n == -1) {
            break;
        }

        for (int i = 0; i < n; i++) {
            scanf("%d", &troops[i]);
        }

        std::sort(troops, troops+n);

        int count = 0;
        int i = 0;

        while (i < n) {
            // s 是没有被覆盖的最左的点的位置
            int s = troops[i++];

            // 一直向右前进直到距s的距离大于R的点
            while (i < n && troops[i] <= s+R) {
                i++;
            }

            // p 是新加上标记的点的位置
            int p = troops[i-1];

            // 一直向右前进直到距p的距离大于R的点
            while (i < n && troops[i] <= p+R) {
                i++;
            }

            count++;
        }

        printf("%d\n", count);

    }

    return 0;
}
