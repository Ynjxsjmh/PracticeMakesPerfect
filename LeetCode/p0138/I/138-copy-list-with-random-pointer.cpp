// 标签：链表、哈希表

Node* copyRandomList(Node* head) {
    if (head == nullptr) {
        return nullptr;
    }

    Node* cur = head;

    while (cur != nullptr) {
        // 扩充二倍
        Node* next = new Node(cur->val, cur->next, nullptr);
        cur->next = next;
        cur = cur->next->next;
    }

    cur = head;
    while (cur != nullptr) {
        // 连接 random
        if (cur->random != nullptr) {
            cur->next->random = cur->random->next;
        }
        cur = cur->next->next;
    }

    cur = head;
    Node* h = head->next;

    while (cur->next != nullptr) {
        // 分离新node，也要保证原node不变
        Node* temp = cur->next;
        cur->next = cur->next->next;
        cur = temp;
    }

    return h;
}