vector<int> PrintFromTopToBottom(TreeNode* root) {
    queue<TreeNode*> q;
    vector<int> result;

    if (root != nullptr) {
        q.push(root);
    }

    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();
        result.push_back(cur->val);

        if (cur->left != nullptr) {
            q.push(cur->left);
        }

        if (cur->right!= nullptr) {
            q.push(cur->right);
        }
    }

    return result;
}