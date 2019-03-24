int removeDuplicates(vector<int>& nums) {
    int k = 2;
    if(nums.size() <= k ) {
        return nums.size();
    }

    int l = 1;
    int r = 1;
    int count = 1;

    while (r < nums.size()) {
        if (nums[r] != nums[r-1]) {
            count = 1;
            nums[l++] = nums[r];
        } else {
            if (count < k) {
                nums[l++] = nums[r];
                count++;
            }
        }
        r++;
    }

    return l;
}
