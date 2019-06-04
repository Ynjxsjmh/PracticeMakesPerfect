// 分类：树

/*
 1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
不为空时，在转化val所得的字符之后添加一个','作为分割。对于空节点则以 '#' 代替。

 2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树
*/

class Solution {
public:
    char* Serialize(TreeNode *root) {
        string result;
        rec(root, result);

        char* ans = new char[result.length()+1];

        int index = 0;
        for (index = 0; index < result.length(); index++) {
            ans[index] = result[index];
        }
        ans[index] = '\0';

        return ans;
    }

    void rec(TreeNode* root, string& result) {
        if (root == nullptr) {
            result += '#';
            return ;
        }

        result += to_string(root->val);
        result += ',';  // 使用逗号分割节点值（节点值可能是多位数如，10）

        rec(root->left, result);
        rec(root->right, result);
    }

   TreeNode* Deserialize(char *str) {
        TreeNode* root;
        create(root, str);
        return root;
    }

    int i = 0;

    void create(TreeNode* & root, char* str) {
        if (str[i] == '\0') {
            return ;
        }

        if (str[i] == '#') {
            root = nullptr;
            return ;
        }

        int num = 0;
        while(str[i] != '\0' && str[i] != ','){
            num = num*10 + (str[i] - '0');
            i++;
        }

        root = new TreeNode(num);
        i++;
        create(root->left, str);
        i++;
        create(root->right, str);
    }

};

