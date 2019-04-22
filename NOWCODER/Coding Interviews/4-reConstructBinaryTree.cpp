TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
    return construct(pre, vin, 0, 0, pre.size()-1);
}

TreeNode* construct(vector<int> pre, vector<int> in, int preIndex, int inBegin, int inEnd) {
    if (preIndex >= pre.size() || inBegin > inEnd) {
        return nullptr;
    }

    int mid = 0;

    for (int i = 0; i <= in.size()-1; i++) {
        if (in[i] == pre[preIndex]) {
            mid = i;
            break;
        }
    }

    TreeNode* root = new TreeNode(pre[preIndex]);
    root->left  = construct(pre, in, preIndex+1, inBegin, mid-1);
    root->right = construct(pre, in, preIndex+mid-inBegin+1, mid+1, inEnd);

    return root;
}