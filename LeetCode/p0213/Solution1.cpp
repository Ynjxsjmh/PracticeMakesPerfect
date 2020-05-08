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
 * @since  2020-05-08 16:10
 * @tag    DP
 * @repeat
 */




class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];

        vector<int> withoutFirst = vector<int>(nums.begin()+1, nums.end());
        vector<int> withoutLast = vector<int>(nums.begin(), nums.end()-1);

        int result1 = rob_not_circle(withoutFirst);
        int result2 = rob_not_circle(withoutLast);

        return max(result1, result2);
    }

    int rob_not_circle(vector<int> nums) {
        int n = nums.size();
        if(n == 0) return 0;
        if(n == 1) return nums[0];
        vector<int> dp(n, 0);

        // Init
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        // DP
        for (int i = 2; i < n; i++) {
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]);
        }

        return dp[n-1];
    }
};
