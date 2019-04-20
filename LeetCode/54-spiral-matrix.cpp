vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;

    if (matrix.size() == 0) {
        return result;
    }

    int row_begin = 0;
    int row_end = matrix.size() - 1;
    int col_begin = 0;
    int col_end = matrix[0].size() - 1;

    while (row_begin <= row_end && col_begin <= col_end) {
        // 从左往右
        for (int i = col_begin; i <= col_end; i++) {
            result.push_back(matrix[row_begin][i]);
        }
        row_begin++;

        // 从上往下
        for (int i = row_begin; i <= row_end; i++) {
            result.push_back(matrix[i][col_end]);
        }
        col_end--;

        if (row_begin <= row_end) {
            // 从右往左
            for (int i = col_end; i >= col_begin; i--) {
                result.push_back(matrix[row_end][i]);
            }
        }
        row_end--;

        if (col_begin <= col_end) {
            // 从下往上
            for (int i = row_end; i >= row_begin; i--) {
                result.push_back(matrix[i][col_begin]);
            }
        }
        col_begin++;
    }
    return result;
}