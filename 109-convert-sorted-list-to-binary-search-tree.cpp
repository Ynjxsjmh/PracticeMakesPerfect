
TreeNode* sortedListToBST(ListNode* head) {
    return build(head, nullptr);
}

TreeNode* build(ListNode* head, ListNode* tail) {
    if(head == tail) {
        return nullptr;
    }

    ListNode* fast = head;
    ListNode* slow = head;

    while (fast != tail && fast->next != tail) {
        fast = fast->next->next;
        slow = slow->next;
    }

    TreeNode* root = new TreeNode(slow->val);
    root->left = build(head, slow);
    root->right = build(slow->next, tail);

    return root;
}