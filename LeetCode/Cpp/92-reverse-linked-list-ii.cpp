ListNode* reverseBetween(ListNode* head, int m, int n) {
    ListNode* prev = nullptr;
    ListNode* cur = head;

    for (int i = 1; i < m; i++) {
        prev = cur;
        cur = cur->next;
    }

    ListNode* guard = prev;
    ListNode* guard2 = cur;

    for (int i = m; i <= n; i++) {
        ListNode* next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }

    if (guard == nullptr) {
        guard2->next = cur;
        return prev;
    }

    guard->next = prev;
    guard2->next = cur;

    return head;
}