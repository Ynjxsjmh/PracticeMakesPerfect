ListNode* removeNthFromEnd(ListNode* head, int n) {
    if (n <= 0 || head == nullptr) {
        return head;
    }

    ListNode* cur = head;
    int num = 0;

    while (cur != nullptr) {
        cur = cur->next;
        num++;
    }

	if (num == n) {
		return head->next;
	}

    ListNode* prev = head;
    cur = head;

    for (int i = 0; i < num-n; i++) {
        prev = cur;
        cur = cur->next;
    }

    prev->next = cur->next;

    return head;
}