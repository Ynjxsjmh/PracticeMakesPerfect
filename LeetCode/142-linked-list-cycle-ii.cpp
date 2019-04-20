ListNode *detectCycle(ListNode *head) {
    if (head == nullptr) {
        return head;
    }

    ListNode* slow = head;
    ListNode* fast = head;
    int length = 0;
    bool hasCycle = false;

    while (fast->next != nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        length++;
        if (slow == fast) {
            hasCycle = true;
            break;
        }
    }

    if (hasCycle) {
        ListNode* q = head;
        while (slow != q) {
            slow = slow->next;
            q = q->next;
        }
        return q;
    }

    return nullptr;
}
