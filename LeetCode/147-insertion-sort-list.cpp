// 标签：排序、链表

ListNode* insertionSortList(ListNode* head) {
    int len = 0;

    ListNode* last = head;
    ListNode* dummy = new ListNode(0);
    dummy->next = head;

    while (last != nullptr) {
        len++;
        last = last->next;
    }

    last = head;
    for (int i = 1; i < len; i++) {
        // [0, i) 是已排好的

        if (last->next->val > last->val) {
            last = last->next;
        } else {
            ListNode* cur = dummy;

            int step = 0;
            while (cur->next->val < last->next->val && step < i-1) {
                cur = cur->next;
                step++;
            }

            ListNode* aim = last->next;
            last->next = aim->next;
            aim->next = cur->next;
            cur->next = aim;
        }
    }

    return dummy->next;
}
