ListNode* ReverseList(ListNode* pHead) {
    ListNode* cur = pHead;
    ListNode* next = cur->next;

    if (cur == nullptr || next == nullptr) {
        return cur;
    }

    cur->next = nullptr;
    while (cur != nullptr && next != nullptr) {
        ListNode* temp = next->next;
        next->next = cur;
        cur = next;
        next = temp;
    }

    return cur;
}