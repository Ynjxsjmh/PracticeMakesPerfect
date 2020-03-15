// 标签：动态规划

int maxProduct(vector<int>& nums) {
    if (nums.size() <= 0) {
        return 0;
    }

    vector<int> maxdp(nums.size());
    vector<int> mindp(nums.size());

    maxdp[0] = nums[0];
    mindp[0] = nums[0]; // 因为可能存在负数，负负得正，因此也要记录最小的。

    int maxProduct = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] > 0) {
            maxdp[i] = max(maxdp[i-1]*nums[i], nums[i]);
            mindp[i] = min(mindp[i-1]*nums[i], nums[i]);
        } else {
            maxdp[i] = max(mindp[i-1]*nums[i], nums[i]);
            mindp[i] = min(maxdp[i-1]*nums[i], nums[i]);
        }
        maxProduct = max(maxProduct, maxdp[i]);
    }

    return maxProduct;
}
