
void solve(vector<vector<char>>& board) {
    // 将四条边上的 O 及与其相连的 O 改成 W
    int row = board.size();
    if (row == 0) {
        return ;
    }
    int col = board[0].size();

    for (int i = 0; i < col; i++) {
        if (board[0][i] == 'O') {
            dfs(board, 0, i);
        }

        if (board[row-1][i] == 'O') {
            dfs(board, row-1, i);
        }
    }

    for (int i = 0; i < row; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0);
        }

        if (board[i][col-1] == 'O') {
            dfs(board, i, col-1);
        }
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            }

            if (board[i][j] == 'W') {
                board[i][j] = 'O';
            }
        }
    }
}


void dfs(vector<vector<char> >& board, int row, int col) {
    board[row][col] = 'W';

    // 对四个方向进行判断
    // 不会死循环的原因是经过的 O 都被改了，不会再经过
    if (row > 0 && board[row-1][col] == 'O') {
        dfs(board, row-1, col);
    }

    if (row < board.size()-1 && board[row+1][col] == 'O') {
        dfs(board, row+1, col);
    }

    if (col > 0 && board[row][col-1] == 'O') {
        dfs(board, row, col-1);
    }

    if (col < board[0].size()-1 && board[row][col+1] == 'O') {
        dfs(board, row, col+1);
    }
}