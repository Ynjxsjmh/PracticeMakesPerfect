ListNode* partition(ListNode* head, int x) {
    ListNode* small = new ListNode(0);
    ListNode* big = new ListNode(0);
    ListNode* moves = small;
    ListNode* moveb = big;

    while (head) {
        if (head->val < x) {
            moves->next = head;
            moves = moves->next;
        } else {
            moveb->next = head;
            moveb = moveb->next;
        }

        head = head->next;
    }

    moveb->next = nullptr;
    moves->next = big->next;

    return small->next;
}

ListNode* partitionDummy(ListNode* head, int x) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;

    ListNode* target = dummy;

    // 找到连续的最后一个比 x 小的数
    while (target->next != nullptr && target->next->val<x) {
        target = target->next;
    }

    ListNode* cur = target;

    while (cur->next != nullptr) {
        if (cur->next->val < x) {
            ListNode* node = target->next;
            ListNode* next = cur->next->next;
            target->next = cur->next;
            target = target->next;
            target->next = node;
            cur->next = next;
        } else {
            cur = cur->next;
        }
    }
    return dummy->next;
}