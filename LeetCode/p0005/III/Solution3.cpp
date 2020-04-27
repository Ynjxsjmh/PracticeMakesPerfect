/**
 * Description
 * Given a string **s**, find the longest palindromic substring in **s**.
 * You may assume that the maximum length of **s** is 1000.
 *
 * Example 1
 * Input:  "babad"
 * Output: "bab"
 * Note:   "aba" is also a valid answer.
 *
 * Example 2
 * Input: "cbbd"
 * Output: "bb"

 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  <2020-04-27 Mon 22:45>
 * @tag    String, DP
 * @repeat
 */


class Solution {
public:
    // 动态规划，时间复杂度O(n^2)，空间复杂度O(n^2)
    string longestPalindrome(string s) {
        const int n = s.size();

        if (n <= 0) {
            return "";
        }

        bool dp[n][n];

        fill_n(&dp[0][0], n*n, false);

        size_t max_len = 1, start = 0;

        for (size_t i = 0; i < s.size(); i++) {
            dp[i][i] = true;

            for (size_t j = 0; j < i; j++) {
                dp[i][j] = (s[j] == s[i] && (i - j < 2 || dp[i-1][j+1]));

                if (dp[i][j] && max_len < (i - j + 1)) {
                    max_len = i - j + 1;
                    start = j;
                }
            }
        }

        return s.substr(start, max_len);
    }
};
