RandomListNode* Clone(RandomListNode* pHead) {
    RandomListNode* dummy = new RandomListNode(0);
    RandomListNode* p = dummy;
    RandomListNode* head = pHead;

    unordered_map<RandomListNode*, RandomListNode*> m;

    while (head) {
        RandomListNode* cur;
        RandomListNode* random;

        if (m.find(head) == m.end()) {
            // 如果表里没有当前节点
            cur = new RandomListNode(head->label);
            m[head] = cur;
        }

        if (head->random != nullptr && m.find(head->random) == m.end()) {
            random = new RandomListNode(head->random->label);
            m[head->random] = random;
        }

        cur = m[head];
        random = m[head->random];
        p->next = cur;
        p->next->random = random;

        head = head->next;
        p = p->next;
    }

    return dummy->next;
}