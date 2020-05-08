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
 * @since  2020-05-08 20:31
 * @tag    DP
 * @repeat
 */

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);

        for (int i = 0; i < n-1; i++) {
            dp[i+1] = max(dp[i], nums[i]) - 1;

            if (dp[i] < 0) return false;
        }

        return dp[n-1] < 0 ? false : true;
    }
};
