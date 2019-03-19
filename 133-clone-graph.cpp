Node* cloneGraph(Node* node) {
    if (!node) {
        return NULL;
    }
    unordered_map<Node*, Node*> mp;
    Node* copy = new Node(node -> val, {});
    mp[node] = copy;
    queue<Node*> q;
    q.push(node);
    while (!q.empty()) {
        Node* cur = q.front();
        q.pop();
        for (Node* neighbor : cur -> neighbors) {
            if (mp.find(neighbor) == mp.end()) {
                // 该节点没有被遍历过
                mp[neighbor] = new Node(neighbor -> val, {});
                q.push(neighbor);
            }
            mp[cur] -> neighbors.push_back(mp[neighbor]);
        }
    }
    return copy;
}