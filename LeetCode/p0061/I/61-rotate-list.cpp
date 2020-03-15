ListNode* rotateRight(ListNode* head, int k) {
    if (head == nullptr)
        return head;

    ListNode* dump = new ListNode(-1);
    dump->next = head;

    int size = 0;
    ListNode* tail = dump;
    while (tail->next != nullptr) {
        size++;
        tail = tail->next;
    }

    k %= size;
    k = size - k;

    if (k != size) {
        ListNode* pre = dump;
        ListNode* cur = pre->next;

        while(k) {
            cur = cur->next;
            pre = pre->next;
            k--;
        }

        tail->next = dump->next;
        dump->next = cur;
        pre->next = nullptr;
    }

    return dump->next;
}