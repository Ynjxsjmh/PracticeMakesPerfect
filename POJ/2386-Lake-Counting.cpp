#include <stdio.h>
#include <string.h>

int a[101][101];
int N, M;

void dfs(int x, int y) {
    a[x][y] = 0;

    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            int nx = x + dx;
            int ny = y + dy;

            if (0 <= nx && nx < N &&
                0 <= ny && ny < M &&
                a[nx][ny] == 1) {
                dfs(nx, ny);
            }
        }
    }
}

int main(int argc, char *argv[]) {
    int result = 0;
    memset(a, 0, sizeof(a));
    scanf("%d%d", &N, &M);

    for (int i = 0; i < N; i++) {
        char s[101];
        scanf("%s", s);

        for (int j = 0; j < M; j++) {
            s[j] == 'W' ? a[i][j] = 1 : a[i][j] = 0;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (a[i][j] == 1) {
                dfs(i, j);
                result++;
            }
        }
    }

    printf("%d\n", result);

    return 0;
}
