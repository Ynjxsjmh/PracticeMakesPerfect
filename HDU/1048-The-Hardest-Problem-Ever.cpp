#include <stdio.h>
#include <string.h>

int main() {
    char str[500];

    while (gets(str)) {
        if (strcmp(str, "ENDOFINPUT") == 0) {
            break;
        }

        if (strcmp(str, "START") == 0 || strcmp(str, "END") == 0) {
            continue;
        }

        int len = strlen(str);

        for (int i = 0; i < len; i++) {
            if (str[i] >= 'F' && str[i] <= 'Z') {
                str[i] -= 5;
            } else if (str[i] >= 'A' && str[i] < 'Z') {
                str[i] += 21;
            } else {
                str[i] = str[i];
            }
        }

        puts(str);
    }

    return 0;
}