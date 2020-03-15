
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int rob(TreeNode* root) {
    deque<TreeNode*> cur;
    deque<TreeNode*> next;
    vector<int> result;

    if (root != nullptr) {
        cur.push_back(root);
    }

    while (!cur.empty()) {
        // sort(cur.begin(), cur.end(), compareTreeNode);
        result.push_back(getSum(cur));

        for (TreeNode* node : cur) {
            if (node->left != nullptr) {
                next.push_back(node->left);
            }

            if (node->right != nullptr) {
                next.push_back(node->right);
            }
        }

        cur = next;
        next.clear();
    }

    return help(result);
}

int help(vector<int>& nums) {
    if (nums.size() <= 0) {
        return 0;
    }

    if (nums.size() == 1) {
        return nums[0];
    }

    vector<int> dp(nums.size(), 0);
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);

    for (int i = 2; i < nums.size(); i++) {
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]);
    }

    return dp[nums.size()-1];
}

static bool compareTreeNode(TreeNode* a, TreeNode* b) {
    return a->val < b->val;
}

int getSum(deque<TreeNode*> d) {
    int sum = 0;

    for (TreeNode* tree : d) {
        sum += tree->val;
    }

    return sum;
}
