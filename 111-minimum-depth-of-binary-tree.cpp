#include <queue>
#include <iostream>

int minDepth(TreeNode* root) {
    int curDepth = 0;
    queue<TreeNode*> q;

    if (root != nullptr) {
        q.push(root);
    }

    while (!q.empty()) {
        int count = q.size();
        curDepth ++;

        for (int i = 0; i < count; i++) {
            TreeNode* cur = q.front();
            q.pop();

            if (cur->left != nullptr) {
                q.push(cur->left);
            }

            if (cur->right != nullptr) {
                q.push(cur->right);
            }

            if (cur->left == nullptr && cur->right == nullptr) {
                return curDepth;
            }
        }
    }
    return curDepth;
}