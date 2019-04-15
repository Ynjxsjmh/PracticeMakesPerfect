int sumNumbers(TreeNode* root) {
    int sum = 0;
    return dfs(root, sum);
}

int dfs(TreeNode* root, int prev) {
    if(root == nullptr)
        return 0;
    int num = prev * 10 + (root->val);
    if(root->left == nullptr && root->right == nullptr)//if node is leaf
        return num;
    else
        return dfs(root->left, num) + dfs(root->right, num);
}