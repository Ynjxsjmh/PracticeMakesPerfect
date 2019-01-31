#include <stack>
#include <vector>
#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    rescrusive(root, result);
    return result;
}

void rescrusive(TreeNode* root, vector<int>& result) {
    if (root != nullptr) {
        rescrusive(root->left, result);
        result.push_back(root->val);
        rescrusive(root->right, result);
    }
}

void non_rescrusive(TreeNode* root, vector<int>& result) {
    stack<TreeNode*> s;
    TreeNode* cur = root;

    while (cur != nullptr || !s.empty()) {
        if (cur != nullptr) {
            s.push(cur);
            cur = cur->left;
        } else {
            cur = s.top();
            s.pop();
            result.push_back(cur->val);
            cur = cur->right;
        }
    }
}