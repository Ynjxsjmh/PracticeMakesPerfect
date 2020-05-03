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
 * @since  2020-05-03 14:51
 * @tag    DP
 * @repeat
 */


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        if (n <= 0) {
            return 0;
        }

        vector<int> dp(n, 0);

        dp[0] = 1;

        for (int i = 1; i < n; i++) {
            int maxval = 0;
            // Find max(dp[j]) 0 <= j < i
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    maxval = max(maxval, dp[j]);
                }
            }

            dp[i] = maxval + 1;
        }

        return *max_element(dp.begin(),dp.end());
    }
};
