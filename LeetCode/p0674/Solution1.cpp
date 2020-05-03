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
 * @since  2020-05-03 20:01
 * @tag    DP
 * @repeat
 */


class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();

        if (n <= 0) {
            return 0;
        }

        vector<int> dp(n, 1);

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i-1]) {
                dp[i] = dp[i-1] + 1;
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};
