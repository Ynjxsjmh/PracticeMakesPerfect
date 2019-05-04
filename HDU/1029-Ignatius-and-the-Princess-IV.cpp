#include <stdio.h>

int main() {
    int number;

    while (~scanf("%d", &number)) {
        int count = 0;
        int candidate = 0;
        int temp;

        for (int i = 0; i < number; i++) {
            scanf("%d", &temp);
            if (count == 0) {
                candidate = temp;
                count = 1;
            } else if (candidate == temp) {
                count++;
            } else {
                count--;
            }
        }

        printf("%d\n", candidate);
    }

    return 0;
}