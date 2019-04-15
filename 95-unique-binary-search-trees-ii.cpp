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
    // 生成一颗 BST 就是选取当前树的根，以及其子树。根的不同会导致不同的 BST
    if(n == 0) return vector<TreeNode*>(0);
    return generateBST(1, n);
}

vector<TreeNode*> generateBST(int left, int right) {
    vector<TreeNode*> result;

    if (left > right) {
        result.push_back(nullptr);
        return result;
    }

    for (int i = left; i <= right; i++) {
        vector<TreeNode*> lefts = generateBST(left, i-1);
        vector<TreeNode*> rights = generateBST(i+1, right);

        for (int j = 0; j < lefts.size(); j++) {
            for (int k = 0; k < rights.size(); k++) {
                TreeNode* root = new TreeNode(i);
                root->left = lefts[j];
                root->right = rights[k];
                result.push_back(root);
            }
        }
    }

    return result;
}