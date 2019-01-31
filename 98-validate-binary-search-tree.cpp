bool isValidBST(TreeNode* root) {
    vector<int> result;
    inorder(root, result);

	if (result.size() == 0 || result.size() == 1) {
		return true;
	}

	if (result.size() == 2) {
		return result[0] < result[1];
	}

    for (int i = 1; i < result.size()-1; i++) {
        if (result[i] > result[i+1] || result[i] < result[i-1]) {
            return false;
        }
    }

    return true;
}

void postorder(TreeNode* root, vector<int>& result) {
    if (root != nullptr) {
        inorder(root->left, result);
		result.push_back(root->val);
        inorder(root->right, result);
    }
}