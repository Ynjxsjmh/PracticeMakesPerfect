ListNode* deleteDuplication(ListNode* pHead) {
    ListNode* cur = pHead;
    ListNode* dummy = new ListNode(0);
    dummy->next = pHead;
    ListNode* pre = dummy;

    while (cur != nullptr && cur->next != nullptr) {
        if (cur->next->val == cur->val) {
            while (cur != nullptr && cur->val == pre->next->val) {
                cur = cur->next;
            }
            pre->next = cur;
        } else {
            cur = cur->next;
            pre = pre->next;
        }
    }

    return dummy->next;
}
