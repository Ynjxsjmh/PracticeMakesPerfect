int minSubArrayLen(int s, vector<int>& nums) {
    int r = 0;
    int l = 0;
    int minLength = INT_MAX;
    int sum = 0;

    while (r < nums.size()) {
        sum += nums[r++];

        while (sum >= s) {
            minLength = min(minLength, r-l);
            sum -= nums[l++];
        }
    }

    return minLength == INT_MAX ? 0 : minLength;
}