// 分类：树

vector<vector<int> > Print(TreeNode* pRoot) {
    vector<vector<int> > result;
    queue<TreeNode*> qcur;  // 当前层的节点

    if (pRoot != nullptr) {
        qcur.push(pRoot);
    }

    while (!qcur.empty()) {
        queue<TreeNode*> qnext; // 下一层的节点
        vector<int> vval;

        while (!qcur.empty()) {
            TreeNode* cur = qcur.front();
            vval.push_back(cur->val);
            qcur.pop();

            if (cur->left!= nullptr) {
                qnext.push(cur->left);
            }

            if (cur->right!= nullptr) {
                qnext.push(cur->right);
            }
        }

        qcur = qnext;
        result.push_back(vval);
    }

    return result;
}
