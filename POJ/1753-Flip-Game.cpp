// http://www.voidcn.com/article/p-dyzyzuhm-bcs.html
#include <stdio.h>

int chess[4][4];
int flag = 0;
int step = 999999;

void turn(int x, int y) {    // 翻转
    if (x >= 0 && x <= 3 && y >= 0 && y <= 3) {
        chess[x][y] = !chess[x][y];
    }
}

void flip(int row, int col) {
    turn(row, col);
    turn(row+1, col);
    turn(row, col+1);
    turn(row-1, col);
    turn(row, col-1);
}

int isComplete() {
    int sum = 0;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            sum += chess[i][j];
        }
    }

    if (sum%16 != 0) {
        return 0;
    } else {
        return 1;  // 都一个色了
    }
}

void dfs(int row, int col, int depth) {
    if (isComplete()) {
        if (step > depth) {
            step = depth;
        }

        return ;
    }

    if (row >= 4 || col >= 4) {
        return ;
    }

    int nx = (row+1)%4;
    int ny = col + (row+1)/4;  // 一列一列的进行

    dfs(nx, ny, depth);  // 当前棋子没有翻转，继续进行
    flip(row, col);

    dfs(nx, ny, depth+1);  // 当前棋子翻转，继续进行
    flip(row, col);

	return;
}

int main() {
    for (int i = 0; i < 4; i++) {
        char s[5];
        scanf ("%s", s);

        for (int k = 0; k < 4; k++){
            if (s[k] == 'b') {
                chess[i][k] = 1;
            }
            else {
                chess[i][k] = 0;
            }
        }
    }

    dfs(0, 0, 0);

    if (step == 999999) {
        printf("Impossible\n");
    }
    else {
        printf("%d\n", step);
    }

    return 0;
}