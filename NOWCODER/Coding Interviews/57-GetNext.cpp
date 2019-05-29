// 分类：树

// 因为有父节点的条件，因此可以通过不断找父节点找到根节点
TreeLinkNode* GetNext(TreeLinkNode* pNode) {
    if (pNode == nullptr) {
        return nullptr;
    }

    if (pNode->right != nullptr) {
        // 如果有右子树，那么找右子树中的最左节点
        pNode = pNode->right;

        while (pNode->left != nullptr) {
            pNode = pNode->left;
        }

        return pNode;
    }

    while (pNode->next != nullptr) {
        // 如果没有右子树，则找第一个当前节点是父节点左孩子的节点
        if (pNode->next->left == pNode) {
            return pNode->next;
        }

        pNode = pNode->next;
    }

    return nullptr;
}