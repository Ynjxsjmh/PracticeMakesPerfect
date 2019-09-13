bool isSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
    if (pRoot2 == nullptr) {
        return false;
    }

    queue<TreeNode*> q;

    if (pRoot1 != nullptr) {
        q.push(pRoot1);
    }

    while (!q.empty()) {
        TreeNode* cur = q.front();
        q.pop();

        if (isSame(cur, pRoot2)) {
            return true;
        }

        if (cur->left != nullptr) {
            q.push(cur->left);
        }

        if (cur->right!= nullptr) {
            q.push(cur->right);
        }
    }

    return false;
}

bool isSame(TreeNode* a, TreeNode* b) {
    if (a == nullptr && b == nullptr) {
        return true;
    }

    if (a == nullptr || b == nullptr) {
        return false;
    }

    if (a->val != b->val) {
        return false;
    }

    return isSame(a->left, b->left) & isSame(a->right, b->right);
}