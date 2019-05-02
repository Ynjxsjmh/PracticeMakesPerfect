bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
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

bool isSubtree(TreeNode* a, TreeNode* b) {
    if (b == nullptr) {
        return true;  // 子树遍历完成（关键语句）
    }

    if (a == nullptr) {
        return false; // 主树异常时的输出（关键语句：提高鲁棒性）
    }

    if (a->val != b->val) {
        return false;
    }

    return isSame(a->left, b->left) & isSame(a->right, b->right);
}