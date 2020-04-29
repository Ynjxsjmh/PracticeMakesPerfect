/**
 * Description
 *
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-04-29 20:22
 * @tag    DP, String
 * @repeat
 */



class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        size_t len1 = text1.size();
        size_t len2 = text2.size();
        size_t dp[len1+1][len2+1];

        fill_n(&dp[0][0], (len1+1)*(len2+1), 0);

        // Unnecessary init
        for (size_t i = 0; i < len1+1; i++) {
            dp[i][0] = 0;
        }

        for (size_t j = 0; j < len2+1; j++) {
            dp[0][j] = 0;
        }

        // DP
        for (size_t i = 1; i < len1+1; i++) {
            for (size_t j = 1; j < len2+1; j++) {
                if (text1[i-1] == text2[j-1]) {
                    // 因为 0 行 0 列代表空字符串，所以这里 i 没必要从 0 开始，从 1 开始，而 C 的字符串索引从 0 开始，要减 1
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        return dp[len1][len2];
    }
};
