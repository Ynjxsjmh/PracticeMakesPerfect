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
 * @since  2020-05-07 23:08
 * @tag    DP
 * @repeat
 */


class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // [3,33,333]
        // 10000
        // 这个 case 用 int 会溢出
        vector<unsigned> dp(target+1, 0);

        // Init
        dp[0] = 1;

        // DP
        for (int i = 1; i < target+1; i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i >= nums[j]) {
                    dp[i] += dp[i-nums[j]];
                }
            }
        }

        return dp[target];
    }
};
