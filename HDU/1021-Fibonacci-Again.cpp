#include <stdio.h>
#include <string.h>

const int m = 2;

struct Matrix{
    int x[m][m];
};

Matrix multiply(Matrix a, Matrix b) {
    Matrix result;
    memset(result.x, 0, sizeof(result.x));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < m; k++) {
                result.x[i][j] += (a.x[i][k] * b.x[k][j]);
                result.x[i][j] %= 3;  // 不取余就 WA，估计溢出。。
            }
        }
    }

    return result;
}

Matrix powerMatrix(Matrix matrix, int n) {
    Matrix temp;
    memset(temp.x, 0, sizeof(temp.x));

    for (int i = 0; i < m; i++) {
        temp.x[i][i] = 1;  // 单位矩阵
    }

    while (n) {
        if (n % 2 == 1) {
            temp = multiply(temp, matrix);
        }

        matrix = multiply(matrix, matrix);
        n /= 2;
    }

    return temp;
}

int main() {
    int n;

    while (~scanf("%d", &n)) {
        Matrix matrix;
        matrix.x[0][0] = 1;
        matrix.x[0][1] = 1;
        matrix.x[1][0] = 1;
        matrix.x[1][1] = 0;

        matrix = powerMatrix(matrix, n-1);

        int fn = 11*matrix.x[0][0] + 7*matrix.x[0][1];

        if (fn % 3 == 0) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }

    return 0;
}