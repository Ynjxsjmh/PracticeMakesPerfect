#include <stdio.h>

int main(int argc, char *argv[])
{
    int k;

    while (~scanf("%d", &k)) {
        int a;

        for (a = 1; a <= 65; ++a) {
            if ((18+a*k) % 65 == 0) {
                printf("%d\n", a);
                break;
            }
        }

        if (a >= 66) {
            printf("no\n");
        }
    }

    return 0;
}
