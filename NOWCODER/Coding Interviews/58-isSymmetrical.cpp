// 分类：树

bool isSymmetrical(TreeNode* pRoot) {
    if (pRoot == nullptr) {
        return true;
    }

    return helper(pRoot->left, pRoot->right);
}

bool helper(TreeNode* t1, TreeNode* t2) {
    if (t1 == nullptr && t2 == nullptr) {
        return true;
    }

    if (t1 != nullptr && t2 != nullptr) {
        return t1->val == t2->val && helper(t1->left, t2->right) && helper(t1->right, t2->left);
    }

    return false;
}