vector<int> printListFromTailToHead(ListNode* head) {
    vector<int> result;

    ListNode* cur = head;

    while (cur != nullptr) {
        result.insert(result.begin(), cur->val);
        cur = cur->next;
    }

    return result;
}