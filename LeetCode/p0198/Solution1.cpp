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
 * @since  2020-05-08 14:56
 * @tag    DP
 * @repeat
 */

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        vector<int> dp(n+1, 0);

        // Init
        dp[0] = 0;
        dp[1] = nums[0];

        // DP
        for (int i = 1; i < n; i++) {
            dp[i+1] = max(dp[i], dp[i-1]+nums[i]);
        }

        return dp[n];
    }
};
