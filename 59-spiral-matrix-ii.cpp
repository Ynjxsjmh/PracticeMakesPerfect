vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> result(n, vector<int>(n,0));

    if (n == 0) {
        return result;
    }

    int row_begin = 0;
    int row_end = n-1;
    int col_begin = 0;
    int col_end = n-1;
    int count = 1;

    while (row_begin <= row_end && col_begin <= col_end) {
        for (int i = col_begin; i <= col_end; i++) {
            // 从左向右
            result[row_begin][i] = count++;
        }
        row_begin++;

        for (int i = row_begin; i <= row_end; i++) {
            // 从上向下
            result[i][col_end] = count++;
        }
        col_end--;

        if (row_begin <= row_end) {
            for (int i = col_end; i >= col_begin; i--) {
                // 从右往左
                result[row_end][i] = count++;
            }
        }
        row_end--;

        if (col_begin <= col_end) {
            for (int i = row_end; i >= row_begin; i--) {
                // 从下往上
                result[i][col_begin] = count++;
            }
        }
        col_begin++;
    }
    return result;
}