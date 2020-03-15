bool isSymmetric(TreeNode* root) {
    return isMirror(root, root);
}

bool isMirror(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) {
        return true;
    }

    if (p == nullptr || q == nullptr) {
        return false;
    }

    return p->val == q->val && isMirror(p->left, q->right) && isMirror(p->right, q->left);
}