vector<vector<string>> solveNQueens(int n) {
    vector<string> chessboard(n, string(n, '.'));

    vector<vector<string>> result;

    dfs(chessboard, 0, result);

    return result;
}

void dfs(vector<string>& chessboard, int row, vector<vector<string>>& result) {
    if (row == chessboard.size()) {
        result.push_back(chessboard);
        return;
    }

    for (int col = 0; col < chessboard.size(); col++) {
        if (validate(chessboard, row, col)) {
            chessboard[row][col] = 'Q';
            dfs(chessboard, row+1, result);
            chessboard[row][col] = '.';
        }
    }
}

bool validate(vector<string>& chessboard, int row, int col) {
    /* 逐行扫描
     * 新的皇后不能在之前皇后的同一列上，即 col != j
     * 新的皇后不能在之前皇后的同一对角线上：
     *     - 一条对角线是 y = x + b
     *     - 一条对角线是 y = -x + b
     * 不妨设原来某一皇后是 (i,j)，新皇后是 (row,col)，对角线是 y = x + b
     * 则有 j = i + b 以及 col = row + b
     * 相减消去 b 可得 j - col = i - row
     */
    for (int i = 0; i < row; i++) {
        // 因为是逐行扫描，当前行是 row，故不必扫描到 row
        for (int j = 0; j < chessboard.size(); j++) {
            if (chessboard[i][j] == 'Q' && ((col == j) || (row + col == i + j) || (row + j == col + i))) {
                return false;
            }
        }
    }

    return true;
}
