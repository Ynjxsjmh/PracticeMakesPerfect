#include <queue>
#include <iostream>
using namespace std;

vector<vector<int>> levelOrderBottom(TreeNode* root) {
    vector<vector<int> > result;
    queue<TreeNode*> q;

    if (root != nullptr) {
        q.push(root);
    }

    while (!q.empty()) {
        int count = q.size();
        result.insert(result.begin(), vector<int> ());

        for (int i = 0; i < count; i++) {
            TreeNode* cur = q.front();
            q.pop();

            result.front().push_back(cur->val);

            if (cur->left != nullptr) {
                q.push(cur->left);
            }

            if (cur->right != nullptr) {
                q.push(cur->right);
            }
        }
    }

    return result;
}