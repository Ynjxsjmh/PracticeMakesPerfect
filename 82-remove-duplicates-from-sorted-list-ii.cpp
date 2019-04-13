ListNode* deleteDuplicates(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;

    ListNode* prev = dummy;
    ListNode* start = dummy->next;
    bool isDulicated = false;

    while (start != nullptr) {

        if (start->next == nullptr) {
            prev = prev->next;
            start = start->next;
            continue;
        }

        if (start->val != start->next->val) {
            prev = prev->next;
            start = start->next;
            continue;
        } else {
            isDulicated = true;
            ListNode* next = start->next;
            start->next = next->next;
        }

        // 特殊考虑为最后一个
        if (isDulicated && (start->next == nullptr || start->val != start->next->val)) {
            prev->next = start->next;
            start = prev->next;
            isDulicated = false;
        }
    }

    return dummy->next;
}