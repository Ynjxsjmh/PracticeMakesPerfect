TreeNode* sortedArrayToBST(vector<int>& nums) {
    return build(nums, 0, nums.size()-1);
}

TreeNode* build(vector<int>& nums, int left, int right) {
    if (left > right) {
        return nullptr;
    }

    int mid = left - (left-right) / 2;
    TreeNode* root = new TreeNode(nums[mid]);
    root->right = build(nums, mid+1, right);
    root->left = build(nums, left, mid-1);

    return root;
}