ListNode* swapPairs(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;

    ListNode* pre = dummy;
    ListNode* in = dummy->next;
    ListNode* post = in == nullptr ? in :in->next;

    while (post != nullptr) {
        in->next = post->next;
        post->next = in;
        pre->next = post;

        pre = pre->next->next;
        in = pre->next;
        post = in == nullptr ? in :in->next;
    }

    return dummy->next;
}