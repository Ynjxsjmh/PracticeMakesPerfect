vector<vector<int> > Print(TreeNode* pRoot) {
    vector<vector<int> > result;
    deque<TreeNode*> dcur;  // 记录上一层的节点
    int depth = 0;

    if (pRoot != nullptr) {
        dcur.push_back(pRoot);
    }

    while (!dcur.empty()) {
        deque<TreeNode*> next; // cur的下一层节点
        vector<int> vcur;
        depth++;  // 因为插入的是下一层的节点，所以提前++
        while (!dcur.empty()) {
            TreeNode* cur = dcur.front();
            vcur.push_back(cur->val);
            dcur.pop_front();

            if (depth % 2 == 0) {
                // 偶数层先右节点后左节点
                if (cur->right!= nullptr) {
                    next.push_front(cur->right);
                }
                if (cur->left != nullptr) {
                    next.push_front(cur->left);
                }
            } else {
                // 奇数层先左节点后右节点
                if (cur->left!= nullptr) {
                    next.push_front(cur->left);
                }
                if (cur->right!= nullptr) {
                    next.push_front(cur->right);
                }
            }

        }

        dcur = next;
        result.push_back(vcur);
    }

    return result;
}