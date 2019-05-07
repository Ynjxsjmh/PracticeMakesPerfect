#include <stdio.h>

int main() {
    int n, u, d;

    while (~scanf("%d%d%d", &n, &u, &d) && n != 0) {
        int time = 0;
        int dis = 0;

        while (1) {
            dis += u;
            time ++;

            if (dis >= n) {
                break;
            }

            dis -= d;
            time ++;
        }

        printf("%d\n", time);
    }

    return 0;
}