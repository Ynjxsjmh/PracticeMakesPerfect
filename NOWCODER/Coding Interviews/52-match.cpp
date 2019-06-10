bool match(char* str, char* pattern) {
    int m = strlen(str);
    int n = strlen(pattern);

    vector<vector<bool> > dp(m+1, vector<bool>(n+1, false));
    dp[0][0]=true;

    for (int i = 0; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (pattern[j-1] == '*') {
                // * 匹配0次或至少匹配一次
                dp[i][j] = dp[i][j-2] || (i && dp[i-1][j] && (str[i-1] == pattern[j-2] || pattern[j-2] == '.') );
            } else {
                dp[i][j] = i && dp[i-1][j-1] && (str[i-1] == pattern[j-1] || pattern[j-1] == '.');
            }
        }
    }

    return dp[m][n];
}