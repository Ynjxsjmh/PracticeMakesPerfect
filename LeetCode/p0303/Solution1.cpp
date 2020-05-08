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
 * @since  2020-05-08 22:51
 * @tag    DP
 * @repeat
 */

class NumArray {
public:
    vector<int> dp;

    NumArray(vector<int>& nums) {
        int cur_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            cur_sum += nums[i];
            dp.push_back(cur_sum);
        }
    }

    int sumRange(int i, int j) {
        if(i == 0)
            return dp[j];

        return dp[j] - dp[i - 1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
