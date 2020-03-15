#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int> > result;
    if (root == nullptr) {
        return result;
    }
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int count = q.size();
        vector<int> tempResult;

        while (count > 0) {
            TreeNode* node = q.front();
            q.pop();
            tempResult.push_back(node->val);
            if (node->left != nullptr) {
                q.push(node->left);
            }

            if (node->right != nullptr) {
                q.push(node->right);
            }

            count--;
        }

        result.push_back(tempResult);
    }

    return result;
}