vector<vector<int>> pathSum(TreeNode* root, int sum) {
    vector<vector<int> > result;
    vector<int> tempResult;

    helper(root, sum, 0, result, tempResult);

    return result;
}

void helper(TreeNode* root, int sum, int curSum, vector<vector<int> >& result, vector<int>& tempResult) {
    if (root == nullptr) {
        return;
    }

    tempResult.push_back(root->val);


    if (root->left == nullptr && root->right == nullptr && root->val + curSum == sum) {
        result.push_back(tempResult);
        // return; // don't add this line.
    }

    helper(root->left, sum, root->val+curSum, result, tempResult);
    helper(root->right, sum, root->val+curSum, result, tempResult);

    tempResult.pop_back();
}