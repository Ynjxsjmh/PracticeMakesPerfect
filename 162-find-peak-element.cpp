int findPeakElement(vector<int>& nums) {
    // https://leetcode.com/problems/find-peak-element/discuss/50222/Sharing-a-more-standard-Binary-Search-C%2B%2B-Solution
    int l = 0;
    int r = nums.size() - 1;

    while (l < r-1) {
        int mid = r - (r-l)/2;

        if (nums[mid] > nums[mid+1] && nums[mid] > nums[mid-1]) {
            return mid;
        } else if (nums[mid] < nums[mid+1]) {
            // mid 不是 peak element
            // 如果，mid+1 比 mid 大，那么 mid 到 r 一定有个 peak element
            l = mid + 1;
        } else {
            // 如果，mid-1 比 mid 大，那么 l 到 mid-1 一定有个 peak element
            r = mid - 1;
        }
    }

    return nums[l] > nums[r] ? l : r;
}
