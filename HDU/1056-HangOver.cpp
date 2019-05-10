#include <stdio.h>
#include <string.h>

int main() {
    double len;
    double a[300];

    memset(a, 0.0, sizeof(a));

    for (int i = 1; i < 300; i++) {
        a[i] += a[i-1] + double(1)/(i+1);
    }

    while (~scanf("%lf", &len)) {
        if (len - 0 < 0.00000000001) {
            break;
        }

        int l = 0;
        int r = 300;

        while (l < r) {
            int mid = l + (r-l)/2;
            if (a[mid] < len) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        printf("%d card(s)\n", r);
    }

    return 0;
}