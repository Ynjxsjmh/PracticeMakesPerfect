int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    int m = obstacleGrid.size();
    int n = obstacleGrid[0].size();

    vector<vector<unsigned>> dp(m, vector<unsigned> (n, 0));

    // 因为只能是往右或往下，所以第一行和第一列中出现一个障碍时
    // 这个障碍后面的砖都不可能再走到，即机会为 0
    for (int i = 0; i < m; i++) {
        if (obstacleGrid[i][0] == 0) {
            dp[i][0] = 1;
        } else {
            break;
        }
    }

    for (int j = 0; j < n; j++) {
        if (obstacleGrid[0][j] == 0) {
            dp[0][j] = 1;
        } else {
            break;
        }
    }

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[i][j] == 0) {
                // 如果当前这块砖是障碍，不计算通过数，即保持初始值 0
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }

    return dp[m-1][n-1];
}