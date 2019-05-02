#include <stdio.h>

int main() {
    int step, mod;

    while (~scanf("%d%d", &step, &mod)) {
        int count = 0;
        int begin = 0;

        do {
            begin = (begin+step)%mod;
            count++;
        } while (begin != 0);

        if (count == mod) {
            printf("%10d%10d    Good Choice\n\n", step, mod);
        } else {
            printf("%10d%10d    Bad Choice\n\n", step, mod);
        }
    }

    return 0;
}