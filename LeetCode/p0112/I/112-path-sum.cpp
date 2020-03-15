bool hasPathSum(TreeNode* root, int sum) {
    return helper(root, sum, 0);
}

bool helper(TreeNode* root, int sum, int curSum) {
    if (root == nullptr) {
        return false;
    }

    if (root != nullptr && root->left == nullptr && root->right == nullptr && root->val + curSum == sum) {
        return true;
    }

    return helper(root->left, sum, curSum+root->val) || helper(root->right, sum, curSum+root->val);
}
