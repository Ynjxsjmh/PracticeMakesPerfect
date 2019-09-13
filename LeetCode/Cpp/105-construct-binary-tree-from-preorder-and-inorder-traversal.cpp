// preorder第一个元素为root，在inorder里面找到root，在它之前的为左子树（长l1），之后为右子树（长l2）
// preorder[1]到preorder[l1]为左子树,之后为右子树，分别递归。
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    return build(preorder, inorder, 0, 0, preorder.size()-1);
}


TreeNode* build(vector<int>& preorder, vector<int>& inorder, int preIndex, int inLeft, int inRight) {
    if (preIndex > preorder.size() - 1 || inLeft > inRight) {
        return nullptr;
    }
    TreeNode* root = new TreeNode(preorder[preIndex]);
    vector<int>::iterator it = find(inorder.begin(), inorder.end(), preorder[preIndex]);
    int mid = distance(inorder.begin(), it);
    root->left = build(preorder, inorder, preIndex+1, inLeft, mid-1);
    root->right = build(preorder, inorder, preIndex+mid-inLeft+1, mid+1, inRight);
    return root;
}
