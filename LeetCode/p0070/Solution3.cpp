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
 * @since  2020-05-01 21:10
 * @tag    DP
 * @repeat
 */


class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int dp[n+1];
        fill_n(&dp[0], (n+1), 0);
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }

        return dp[n];
    }
};
