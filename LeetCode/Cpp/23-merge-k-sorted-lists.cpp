ListNode* mergeKLists(vector<ListNode*>& lists) {
//tNode dummy(0);
//tNode* cur = &dummy;
//
// (int i = 0; i < lists.size(); i=i++) {
// cur->next = mergeTwoLists(cur->next, lists[i]);
// cur = cur->next == nullptr ? cur : cur->next;
//
//
//urn dummy.next;
//
//
	if (lists.empty()){
	  return nullptr;
	}
	while (lists.size() > 1) {
		lists.push_back(mergeTwoLists(lists[0], lists[1]));
		lists.erase(lists.begin());
		lists.erase(lists.begin());
	}

	return lists[0];

}

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* cur = &dummy;

    while (l1 != nullptr && l2 != nullptr) {
        if(l1->val < l2->val) {
            cur->next = l1;
            l1 = l1->next;
        } else {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
    }

    cur->next = l1 != nullptr ? l1 : l2;

    return dummy.next;
}