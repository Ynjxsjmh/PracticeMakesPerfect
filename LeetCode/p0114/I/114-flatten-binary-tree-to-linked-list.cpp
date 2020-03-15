void flatten(TreeNode* root) {
    if (root != nullptr && root->left != nullptr) {
        TreeNode* right = root->left;

        while(right->right != nullptr) {
            right = right->right;
        }

        right->right = root->right;

        root->right = root->left;

        root->left = nullptr;
    }

    if (root != nullptr && root ->right != nullptr) {
        flatten(root->right);
    }
}