ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
    int length = 0;
    ListNode* cur = pListHead;

    while (cur != nullptr) {
        cur = cur->next;
        length++;
    }

    int move = length - k;

    if (k > length) {
        return nullptr;
    }

    while(move > 0) {
        pListHead = pListHead->next;
        move--;
    }

    return pListHead;
}