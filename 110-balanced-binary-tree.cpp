bool isBalanced(TreeNode* root) {
    if (root == nullptr) {
        return true;
    }

    if (abs(depth(root->right)-depth(root->left) > 1)) {
        return false;
    }

    return isBalanced(root->right) && isBalanced(root->left);
}

int depth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int rightDepth = depth(root->right);
    int leftDepth = depth(root->left);

    return max(rightDepth, leftDepth) + 1;
}