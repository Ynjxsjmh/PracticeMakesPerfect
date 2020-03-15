bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == word[0]) {
                // std::cout<<"i="<<i<<" "<<"j="<<j<<std::endl;
                if (find(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
    }

    return false;
}

bool find(vector<vector<char>>& board, int row, int col, string word, int index) {
    if (index == word.size()) {
        return true;
    }

    if (row < 0 || col < 0 || row >= board.size() || col >= board[0].size()) {
        return false;
    }

    if (board[row][col] != word[index]) {
        return false;
    }

    // std::cout<<"row="<<row<<" "<<"col="<<col<<" "<<"index="<<index<<std::endl;
    // std::cout<<board[row][col]<<" "<<word[index]<<std::endl;

    board[row][col] |= 128;  // 标记已经走过的，位运算会快点
    // board[row][col] += 32;  // 标记已经走过的，变小写 超时
    // std::cout<<board[row][col]<<std::endl;

    // 像下面这样写，避免超时
    bool exsists = find(board, row+1, col, word, index+1) ||
        find(board, row-1, col, word, index+1) ||
        find(board, row, col+1, word, index+1) ||
        find(board, row, col-1, word, index+1);
    // board[row][col] -= 32;  // 标记已经走过的，变小写
    board[row][col] &= 127;

    return exsists;
}