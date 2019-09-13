int findMin(vector<int>& nums) {
    int min = nums[0];
    int l = 0;
    int r = nums.size()-1;

    while (l <= r) {
        int mid = r-(r-l)/2;

        if (nums[mid] < min) {
            min = nums[mid];
        }

        if (nums[l] < min) {
            min = nums[l];
        }

        if (nums[r] < min) {
            min = nums[r];
        }

        if (nums[mid] > nums[l]) {
            // 左边有序，最小值不可能在左边出现
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return min;
}
