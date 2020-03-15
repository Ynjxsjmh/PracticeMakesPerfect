vector<int> searchRange(vector<int>& nums, int target) {
    set<int> res;
    vector<int> ans;

    search(nums, 0, nums.size()-1, target, res);

    if (res.size() == 0) {
        ans.push_back(-1);
        ans.push_back(-1);
    } else if (res.size() == 1) {
        ans.push_back(*res.begin());
        ans.push_back(*res.begin());
    } else {
        ans.push_back(*res.begin());
        ans.push_back(*(--res.end()));
    }

    return ans;
}

void search(vector<int>& nums, int l, int r, int target, set<int>& res) {
    if (l > r) {
        return;
    }

    int mid = r - (r-l)/2;

    if (nums[mid] == target) {
        res.insert(mid);
    }

    search(nums, l, mid-1, target, res);
    search(nums, mid+1, r, target, res);
}