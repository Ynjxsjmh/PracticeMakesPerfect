/*
subsets([1,2,3,4]) = []
                     // push(1)
                     [1, subsets([2,3,4])] // if push N times in subsets([2,3,4]), the pop times is also N, so vec is also [1] after backtrack.
                     // pop(), push(2)
                     [2, subsets([3,4])]
                     // pop(), push(3)
                     [3, subsets([4])]
                     // pop(), push(4)
                     [4, subsets([])]
                     // pop()
 */

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> part;
    sort(nums.begin(), nums.end());

    subset(nums, result, part, 0);

    return result;
}

void subset(vector<int>& nums, vector<vector<int>>& result, vector<int>& part, int begin) {
    result.push_back(part);

    for (int i = begin; i < nums.size(); i++) {
        if (i == begin || nums[i] != nums[i-1]) {
            part.push_back(nums[i]);
            subset(nums, result, part, i+1);
            part.pop_back();
        }
    }
}