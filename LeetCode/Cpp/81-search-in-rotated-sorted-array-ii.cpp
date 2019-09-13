bool search(vector<int>& nums, int target) {
    int l = 0;
    int r = nums.size()-1;

    while (l <= r) {
        int mid = r - (r-l)/2;

        if (nums[mid] == target) {
            return true;
        }

        if (nums[mid] > nums[l]) {
            // l~mid 递增
            if (target >= nums[l] && target < nums[mid]) {
                // target 在 l~mid 中
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        } else if (nums[mid] < nums[l]) {
            // mid~r 递增
            if (target > nums[mid] && target <= nums[r]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        } else {
            l ++;
        }

    }

    return false;
}
