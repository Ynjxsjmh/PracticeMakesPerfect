// 分类：链表，双指针

ListNode* EntryNodeOfLoop(ListNode* pHead) {
    /*
     * ---------
     * b   ^ s e  (b 是 begin，e是end，s是slow fast相遇处，^ 是环开始)
     * b 到s距离为len
     * 不妨设 ^ 到s距离为 x，s到e距离为y
     * 所以fast走的距离为len+x+y = 2len
     * 即 len = x+y
     * 即b到 ^ 距离为s到e的距离
     */
    if (pHead == nullptr) {
        return nullptr;
    }

    ListNode* slow = pHead;
    ListNode* fast = pHead;
    int hasCycle = 0;
    int len = 0;

    while (fast->next != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next;
        len++;

        if (slow == fast) {
            hasCycle = 1;
            break;
        }
    }

    if (hasCycle) {
        ListNode* q = pHead;
        while (q != slow) {
            q = q->next;
            slow = slow->next;
        }

        return q;
    } else {
        return nullptr;
    }
}