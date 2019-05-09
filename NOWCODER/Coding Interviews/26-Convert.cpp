TreeNode* Convert(TreeNode* pRootOfTree) {
    if (pRootOfTree == nullptr) {
        return nullptr;
    }

    TreeNode* pre = nullptr;

    inorder(pRootOfTree, pre);

    TreeNode* result = pRootOfTree;

    while (result->left != nullptr) {
        result=result->left;
    }

    return result;
}

void inorder(TreeNode* cur, TreeNode*& pre) {
    // 中根遍历
    if (cur == nullptr) {
        return;
    }

    inorder(cur->left, pre);

    cur->left = pre;
    if (pre != nullptr) {
        pre->right = cur;
    }
    pre = cur;

    inorder(cur->right, pre);
}