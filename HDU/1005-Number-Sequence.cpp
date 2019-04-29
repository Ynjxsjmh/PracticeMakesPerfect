#include <stdio.h>
#include <string.h>

const int m = 2;
const int mod = 7;
struct Matrix {
    int x[m][m];
};

Matrix multiple(Matrix a, Matrix b) {
    Matrix temp;
    memset(temp.x, 0, sizeof(temp.x));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < m; k++) {
                temp.x[i][j] += a.x[i][k] * b.x[k][j];
                temp.x[i][j] %= mod;
            }
        }
    }

    return temp;
}

// 矩阵快速幂
Matrix powMatrix(Matrix mat, int n) {
    Matrix temp;
    memset(temp.x, 0, sizeof(temp.x));
    for (int i = 0; i < m; i++) {
        temp.x[i][i] = 1; //初始化单位矩阵
    }

    while (n) {
        if (n%2 == 1) {
            temp = multiple(temp, mat);
        }
        mat = multiple(mat, mat);
        n = n/2;
    }

    return temp;
}

int main() {
    int A, B, n;

    while (~scanf("%d%d%d", &A,&B,&n)) {
        if (A == 0 && B == 0 && n ==0) {
            break;
        }

        Matrix mat;

        mat.x[0][0] = A;
        mat.x[0][1] = B;
        mat.x[1][0] = 1;
        mat.x[1][1] = 0;

        mat = powMatrix(mat, n-2);

        printf("%d\n",(mat.x[0][0] + mat.x[0][1])%mod);
    }
}