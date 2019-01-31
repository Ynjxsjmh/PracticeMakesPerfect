/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

vector<TreeNode*> generateTrees(int n) {
    vector<TreeNode*> result;

    generateBST(result, nullptr, 1, n);

    return result;
}

void generateBST(vector<TreeNode*>& result, TreeNode* root, int left, int right) {
    if (left > right) {
        result.push_back(nullptr);
        return;
    }

    for (int i = left; i <= right; i++) {
        root = new TreeNode(i);

        generateBST(result, root->left, left, i-1);
        generateBST(result, root->right, i+1, right);

        result.push_back(root);
    }
}