// 分类：回溯

bool hasPath(char* matrix, int rows, int cols, char* str) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i*cols+j] == str[0]) {
                if (helper(matrix, rows, cols, str, i, j, 0)) {
                    return true;
                }
            }
        }
    }

    return false;
}

bool helper(char* matrix, int rows, int cols, char* str, int x, int y, int index) {
    if (str[index] == '\0') {
        // 匹配完成
        return true;
    }

    if (x > rows || x < 0 || y > cols || y < 0) {
        // 越界判断
        return false;
    }

    if (matrix[x*cols+y] == '-') {
        // 用 - 来表示已经搜索过了
        return false;
    }

    if (matrix[x*cols+y] != str[index]) {
        return false;
    }

    char cur = matrix[x*cols+y];
    // 标记已经走了
    matrix[x*cols+y] = '-';

    // 四个方向
    bool sign = helper(matrix, rows, cols, str, x+1, y, index+1) ||
        helper(matrix, rows, cols, str, x-1, y, index+1) ||
        helper(matrix, rows, cols, str, x, y+1, index+1) ||
        helper(matrix, rows, cols, str, x, y-1, index+1);

    matrix[x*cols+y] = cur;

    return sign;
}