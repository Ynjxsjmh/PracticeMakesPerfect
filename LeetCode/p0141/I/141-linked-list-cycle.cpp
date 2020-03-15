bool hasCycle(ListNode *head) {
    if (head == nullptr) {
        return false;
    }

    ListNode* slow = head;
    ListNode* fast = head;

    while (fast->next!= nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }

    return false;
}