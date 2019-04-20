Node* connect(Node* root) {
    vector<Node*> cur_level;

    if (root != nullptr) {
        cur_level.push_back(root);
    }

    while (!cur_level.empty()) {
        vector<Node*> next_level;

        for (int i = 0; i < cur_level.size(); i++) {

            if (i < cur_level.size()-1) {
                cur_level[i]->next = cur_level[i+1];
            }

            if (cur_level[i]->left != nullptr) {
                next_level.push_back(cur_level[i]->left);
            }

            if (cur_level[i]->right != nullptr) {
                next_level.push_back(cur_level[i]->right);
            }
        }

        cur_level = next_level;
    }

    return root;
}