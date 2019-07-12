// 标签：背包问题、动态规划

int minHeightShelves(vector<vector<int>>& books, int shelf_width) {
    int n = books.size();

    vector<int> dp(n, INT_MAX/2);

    for (int i = 0; i < n; i++) {
        int width = 0;
        int h = 0;
        for (int j = i; j < n; j++) {
            if ((width += books[j][0]) > shelf_width) {
                break;
            }

            h = max(h, books[j][1]);
            dp[j] = min(dp[j], (i == 0 ? 0 : dp[i-1]) + h);
        }
    }

    return dp.back();
}