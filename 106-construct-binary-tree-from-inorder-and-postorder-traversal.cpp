TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    return build(inorder, postorder, postorder.size()-1, 0, inorder.size()-1);

}

TreeNode* build(vector<int>& inorder, vector<int>& postorder, int postIndex, int inLeft, int inRight) {
    if (postIndex < 0 || postIndex > inorder.size()-1 || inLeft > inRight) {
        return nullptr;
    }

    TreeNode* root = new TreeNode(postorder[postIndex]);

    vector<int>::iterator it = find(inorder.begin(), inorder.end(), postorder[postIndex]);
    int mid = distance(inorder.begin(), it);

    root->right = build(inorder, postorder, postIndex-1, mid+1, inRight);
    root->left = build(inorder, postorder, postIndex-(inRight-mid+1), inLeft, mid-1);
    return root;
}