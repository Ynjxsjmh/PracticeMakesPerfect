bool IsBalanced_Solution(TreeNode* pRoot) {
    if (pRoot == nullptr) {
        return true;
    }

    int left = getDepth(pRoot->left);
    int right = getDepth(pRoot->right);

    if (abs(left-right) <= 1) {
        return IsBalanced_Solution(pRoot->left) && IsBalanced_Solution(pRoot->right);
    } else {
        return false;
    }
}

int getDepth(TreeNode* pRoot) {
    if (pRoot == nullptr) {
        return 0;
    }

    int left = getDepth(pRoot->left);
    int right = getDepth(pRoot->right);

    return left > right ? left + 1 : right + 1;
}