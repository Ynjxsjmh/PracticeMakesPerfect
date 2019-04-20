static const auto io_sync_off = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	return nullptr;
}();
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size(), ans;
        vector<int> dp(len);
        ans = dp[0] = nums[0];
        for (int i = 1; i < len; i++) {
            dp[i] = max(nums[i], dp[i - 1] + nums[i]);
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};