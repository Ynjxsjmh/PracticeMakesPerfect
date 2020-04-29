/**
 * Description
 * Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
 *
 * Example1
 * Input:  "bbbab"
 * Output: 4
 * Explanation:  One possible longest palindromic subsequence is "bbbb".
 *
 * Example2
 * Input:  "cbbd"
 * Output: 2
 * Explanation:  One possible longest palindromic subsequence is "bb".
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  <2020-04-29 Wed 15:29>
 * @tag    DP, String
 * @repeat
 */


class Solution {
public:
    int longestPalindromeSubseq(string s) {
        size_t len = s.size();

        if (len <= 0) {
            return 0;
        }

        int dp[len][len];

        // Init
        fill_n(&dp[0][0], len*len, 0);

        for (size_t i = 0; i < s.size(); i++){
            dp[i][i]=1;
        }

        for (size_t i = 0; i < s.size()-1; i++){
            dp[i][i+1]= (s[i] == s[i+1]) ? 2 : 1;
        }

        // DP
        for (int i = len - 2; i >= 0; --i) {
            // size_t i 会溢出
            for (int j = i + 1; j < len; ++j) {
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[0][len-1];
    }
};
