vector<int> postorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> s;

    if (root != nullptr) {
        s.push(root);
    }

    while (!s.empty()) {
        TreeNode* cur = s.top();
        s.pop();

        if (cur->left != nullptr) {
            s.push(cur->left);
        }

        if (cur->right != nullptr) {
            s.push(cur->right);
        }

        result.insert(result.begin(), cur->val);

    }

    return result;
}



vector<int> PostorderTraversal(TreeNode* root) {
    vector<int> result;
    rec(root, result);
    return result;
}

void rec(TreeNode* root, vector<int>& result) {
    if (root == nullptr) {
        return;
    }

    rec(root->left, result);
    rec(root->right, result);
    result.push_back(root->val);
}