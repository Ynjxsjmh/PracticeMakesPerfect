int TreeDepth(TreeNode* pRoot) {
    return rec(pRoot, 0);
}

int rec(TreeNode* pRoot, int depth) {
    if (pRoot == nullptr) {
        return depth;
    }

    int left = rec(pRoot->left, depth+1);
    int right = rec(pRoot->right, depth+1);

    return left < right ? right : left;
}