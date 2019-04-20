ListNode* deleteDuplicates(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    dummy -> next = head;

    ListNode* start = dummy->next;

    while (start != nullptr) {
        if (start->next == nullptr) {
            start = start->next;
            continue;
        }

        if (start->val != start->next->val) {
            start = start->next;
        } else {
            ListNode* next = start->next;
            start->next = next->next;
        }
    }

    return dummy->next;
}