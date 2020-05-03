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
 * @since  2020-05-03 20:45
 * @tag    DP
 * @repeat
 */


class Solution {
public:
    int coinChange (vector<int>& coins, int amount) {
        int n = coins.size();

        if (n <= 0) {
            return 0;
        }

        vector<int> dp(amount+1, INT_MAX-1);

        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < n; j++) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i-coins[j]]+1);
                }
            }
        }

        return dp[amount] == INT_MAX-1 ? -1 : dp[amount];
    }
};
