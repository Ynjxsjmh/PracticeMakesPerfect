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
 * @since  <2020-04-29 Wed 23:46>
 * @tag    DP, String
 * @repeat
 */


class Solution {
public:
    int countSubstrings(string s) {
        const int n = s.size();
        int cnt = 0;

        if (n <= 0) {
            return 0;
        }

        bool dp[n][n];

        fill_n(&dp[0][0], n*n, false);

        for (size_t i = 0; i < n; i++) {
            dp[i][i] = true;
            cnt++;
        }

        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < i; j++) {
                dp[i][j] = (s[j] == s[i] && (i - j < 2 || dp[i-1][j+1]));

                if (dp[i][j]) {
                    cnt++;
                }
            }
        }

        return cnt;
    }
};
