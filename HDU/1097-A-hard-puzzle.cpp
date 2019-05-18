#include <stdio.h>

int main(int argc, char *argv[])
{
    long long a, n; // int n 会溢出

    while (~scanf("%ld%ld", &a, &n)) {
        int result = 1;

        while (n) {
            if (n%2 == 1) {
                result = (result*a)%10;
            }

            a = (a*a)%10;
            n>>=1;
        }

        result %= 10;
        printf("%d\n", result);
    }

    return 0;
}
