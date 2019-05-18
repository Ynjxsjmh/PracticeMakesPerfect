ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2) {
    ListNode* cur1 = pHead1;
    ListNode* cur2 = pHead2;

    vector<ListNode*> v;

    while (cur1 != nullptr) {
        v.push_back(cur1);
        cur1 = cur1->next;
    }

    while (cur2 != nullptr) {
        if (find(v.begin(), v.end(), cur2) != v.end()) {
            return cur2;
        }

        cur2 = cur2->next;
    }

    return nullptr;
}