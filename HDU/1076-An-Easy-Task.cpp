#include <stdio.h>
#include <stdbool.h>

bool isLeapYear(int year) {
    return (year%4 == 0 && year%100 != 0) || year%400==0;
}

int main() {
    int T, Y, N;

    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf("%d%d", &Y, &N);

        int count = 0;

        while (!isLeapYear(Y)) {
            Y++;
        }
        count = 1;

        for (; count < N;) {
            Y += 4;
            if (isLeapYear(Y)) {
                count++;
            }
        }

        printf("%d\n", Y);
    }

    return 0;
}