Node* connect(Node* root) {
    vector<Node*> q;

    if (root != nullptr) {
        q.push_back(root);
    }

    while (!q.empty()) {
        vector<Node*> temp;

        for (int i = 0; i < q.size(); i++) {
            if (i < q.size()-1) {
                q[i]->next = q[i+1];
            }

            if (q[i]->left != nullptr) {
                temp.push_back(q[i]->left);
            }

            if (q[i]->right != nullptr) {
                temp.push_back(q[i]->right);
            }
        }

        q = temp;
    }

    return root;
}