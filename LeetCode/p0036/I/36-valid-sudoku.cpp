bool isValidSudoku(vector<vector<char>>& board) {
    bool rows[9][10] = {false};
    bool cols[9][10] = {false};
    bool cubes[9][10] = {false};

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            if (board[i][j] != '.') {
                int num = board[i][j] - '0';
                int k = i / 3 * 3 + j / 3;

                if (rows[i][num] || cols[j][num] || cubes[k][num]) {
                    return false;
                } else {
                    rows[i][num] = true;
                    cols[j][num] = true;
                    cubes[k][num] = true;
                }
            }
        }
    }
    return true;
}
