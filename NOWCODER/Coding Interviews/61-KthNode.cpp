// 分类：树

// 思路：二叉搜索树按照中序遍历的顺序打印出来正好就是排序好的顺序。
// 所以，按照中序遍历顺序找到第k个结点就是结果。

TreeNode* KthNode(TreeNode* pRoot, int k) {
    vector<TreeNode*> result;

    if (pRoot == nullptr || k <= 0) {
        return nullptr;
    }

    rec(pRoot, result);

    if (k > result.size()) {
        return nullptr;
    }

    return result[k-1];
}

void rec(TreeNode* pRoot, vector<TreeNode*>& result) {
    if (pRoot != nullptr) {
        rec(pRoot->left, result);
        result.push_back(pRoot);
        rec(pRoot->right, result);
    }
}