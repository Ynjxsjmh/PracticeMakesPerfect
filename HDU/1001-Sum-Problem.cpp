#include <cstdio>

int main() {
    int a;

    while (~scanf("%d", &a)) {
        unsigned int sum = (1+a) * a;
        printf("%d\n\n", sum/2);
    }

    return 0;
}