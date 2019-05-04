void Mirror(TreeNode *pRoot) {
    if (pRoot == nullptr) {
        return;
    }

    TreeNode* temp;
    temp = pRoot->left;
    pRoot->left = pRoot->right;
    pRoot->right = temp;

    if (pRoot->right != nullptr) {
        Mirror(pRoot->right);
    }

    if (pRoot->left != nullptr) {
        Mirror(pRoot->left);
    }
}