void nextPermutation(vector<int>& nums) {
    /*
     1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
     2. Find the largest index l > k such that nums[k] < nums[l].
     3. Swap nums[k] and nums[l].
     4. Reverse the sub-array nums[k + 1:].
     */
    int k = nums.size() - 2;
    int l = nums.size() - 1;

    while (k >= 0 && nums[k] >= nums[k+1]) {
        k--;
    }

    if (k < 0 ) {
        return sort(nums.begin(), nums.end());
    }

    while (l > k && nums[l] <= nums[k]) {
        l--;
    }

    swap(nums[l], nums[k]);

    reverse(nums.begin()+k+1, nums.end());
}
