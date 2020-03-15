void sortColors(vector<int>& nums) {
    // https://leetcode.com/problems/sort-colors/discuss/26474/Sharing-C%2B%2B-solution-with-Good-Explanation
    int l = 0;
    int mid = 0;
    int r = nums.size()-1;

    while (mid <= r) {
        if (nums[mid] == 1) {
            mid ++;
        } else if (nums[mid] == 0) {
            swap(nums[mid], nums[l]);
            mid++;
            l++;
        } else if (nums[mid] == 2) {
            swap(nums[mid], nums[r]);
            r--;
        }
    }
}