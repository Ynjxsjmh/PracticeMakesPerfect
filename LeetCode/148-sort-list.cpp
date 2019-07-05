// 标签：排序、链表

ListNode* sortList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode* slow = head;
    ListNode* fast = head->next;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // divide the list into two parts
    fast = slow->next;
    slow->next = nullptr;

    return merge(sortList(head), sortList(fast));
}

ListNode* merge(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;

    while (l1 != nullptr && l2 != nullptr) {
        if (l1->val < l2->val) {
            cur->next = l1;
            l1 = l1->next;
        } else {
            cur->next = l2;
            l2 = l2->next;
        }

        cur = cur->next;
    }

    if (l1 != nullptr) {
        cur->next = l1;
    } else {
        cur->next = l2;
    }

    return dummy->next;
}