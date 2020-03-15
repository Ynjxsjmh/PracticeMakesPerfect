// 标签：动态规划

bool wordBreak(string s, vector<string>& wordDict) {
    if (wordDict.size() == 0) {
        return false;
    }

    vector<bool> dp(s.size()+1, false);  // dp[i] is set to true if a valid word (word sequence) ends there
    dp[0] = true;

    for (int i = 1; i <= s.size(); i++) {
        // 从1开始是因为substr(j, i-j) 如果i为0 时j也为0没啥意义
        for (int j = 0; j < i; j++) {
            if (dp[j]) {
                // dp[j] 为 true 表示，前面已经有一个在wordDict中的单词，只有此时才继续判断
                string word = s.substr(j, i-j); // 从 j 截取到 i

                if (std::find(wordDict.begin(), wordDict.end(), word) != wordDict.end()) {
                    // 如果找到匹配字符
                    dp[i] = true;
                    break;
                }
            }
        }
    }

    return dp[s.size()];
}