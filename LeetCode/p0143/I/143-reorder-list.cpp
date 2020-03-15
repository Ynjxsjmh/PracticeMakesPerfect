// 标签：链表

void reorderList(ListNode* head) {
    int len = 0;

    ListNode* cur = head;

    while (cur != nullptr) {
        len++;
        cur = cur->next;
    }

    if (len <= 2) {
        return;
    }

    cur = head;
    int cur_len = 1;

    while (cur != nullptr && cur_len < len - cur_len) {
        int move = len - 2*cur_len + 1;
        ListNode* pre = cur;

        while (move > 1) {
            pre = pre->next;
            move--;
        }

        ListNode* aim = pre->next;

        pre->next = nullptr;
        aim->next = cur->next;
        cur->next = aim;

        cur = cur->next->next;
        cur_len++;
    }
}