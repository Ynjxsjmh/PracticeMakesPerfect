int totalNQueens(int n) {
    vector<int> cols(n, 0);
    vector<int> mainDiagonal(2*n-1, 0);
    vector<int> subDiagonal(2*n-1, 0);
    int count = 0;
    dfs(0, cols, mainDiagonal, subDiagonal, count);

    return count;
}

void dfs(int row, vector<int>& cols, vector<int>& mainDiagonal, vector<int>& subDiagonal, int& count) {
    if (row == cols.size()) {
        count++;
        return;
    }

    for (int col = 0; col < cols.size(); col++) {
        int id1 = row + col;
        int id2 = col - row + cols.size() - 1;
        if (!cols[col] && !mainDiagonal[id1] && !subDiagonal[id2]) {
            cols[col] = mainDiagonal[id1] = subDiagonal[id2] = 1;
            dfs(row+1, cols, mainDiagonal, subDiagonal, count);
            cols[col] = mainDiagonal[id1] = subDiagonal[id2] = 0;
        }

    }
}
