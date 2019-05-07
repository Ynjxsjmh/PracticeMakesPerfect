vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
    vector<vector<int> > result;
    vector<int> tempResult;

    helper(root, expectNumber, 0, result, tempResult);

    return result;
}

void helper(TreeNode* root, int expectNumber, int sum, vector<vector<int> >& result, vector<int>& tempResult) {
    if (root == nullptr) {
        return;
    }

    sum += root->val;

    tempResult.push_back(root->val);

    if (root->left == nullptr && root->right == nullptr && sum == expectNumber) {
        result.push_back(tempResult);
    }

    helper(root->left, expectNumber, sum, result, tempResult);
    helper(root->right, expectNumber, sum, result, tempResult);
    tempResult.pop_back();
}