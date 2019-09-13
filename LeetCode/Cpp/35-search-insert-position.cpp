int searchInsert(vector<int>& nums, int target) {
    return search(nums, target, 0, nums.size()-1);
}

int search(vector<int>& nums, int target, int l, int r) {
    if (l > r) {
        return l;
    }

    int mid = r - (r-l)/2;

    if (nums[mid] == target) {
        return mid;
    } else if (nums[mid] > target) {
        return search(nums, target, l, mid-1);
    } else {
        return search(nums, target, mid+1, r);
    }
}