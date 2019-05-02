ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    ListNode* cur1 = pHead1;
    ListNode* cur2 = pHead2;

    while (cur1 != nullptr || cur2 != nullptr) {
        int val1 = cur1 == nullptr ? INT_MAX : cur1->val;
        int val2 = cur2 == nullptr ? INT_MAX : cur2->val;
        if (val1 <= val2) {
            cur->next = new ListNode(cur1->val);
            cur1 = cur1->next;
        } else {
            cur->next = new ListNode(cur2->val);
            cur2 = cur2->next;
        }
        cur = cur->next;
    }

    return dummy->next;
}