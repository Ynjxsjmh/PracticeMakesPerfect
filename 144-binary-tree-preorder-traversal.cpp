vector<int> preorderTraversal(TreeNode* root) {
    vector<int> result;
    stack<TreeNode*> s;

    if (root != nullptr) {
        s.push(root);
    }

    while (!s.empty()) {
        TreeNode* cur = s.top();
        s.pop();

        result.push_back(cur->val);

        // 栈是后进先出，所以先push右边的
        if (cur->right != nullptr) {
            s.push(cur->right);
        }

        if (cur->left != nullptr) {
            s.push(cur->left);
        }

    }

    return result;
}

vector<int> PreorderTraversal(TreeNode* root) {
    vector<int> result;
    rec(root, result);
    return result;
}

void rec(TreeNode* root, vector<int>& result) {
    if (root == nullptr) {
        return;
    }

    result.push_back(root->val);
    rec(root->left, result);
    rec(root->right, result);
}