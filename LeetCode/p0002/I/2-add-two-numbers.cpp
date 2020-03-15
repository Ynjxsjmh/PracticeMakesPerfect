ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* result = new ListNode(0);
    ListNode* curr = result;

    int carry = 0;
    while (l1 != nullptr || l2 != nullptr) {
        int val1 = l1 == nullptr ? 0 : l1->val;
        int val2 = l2 == nullptr ? 0 : l2->val;
        int sum = val1 + val2 + carry;

        if (sum >= 10) {
            sum -= 10;
            carry = 1;
        } else {
            carry = 0;
        }

        ListNode* temp = new ListNode(sum);
        curr->next = temp;
        curr = curr->next;
        l1 = l1 == nullptr ? nullptr : l1->next;
        l2 = l2 == nullptr ? nullptr : l2->next;
    }

	if (carry > 0) {
		ListNode* temp = new ListNode(carry);
		curr->next = temp;
	}

    return result->next;
}