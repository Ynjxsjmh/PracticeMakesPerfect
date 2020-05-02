/**
 * Description
 *
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-05-02 01:31
 * @tag    Backtracking
 * @repeat
 */



class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtracking(n, "", result, 0, 0);
        return result;
    }

    // l 是左括号的数目，r 是右括号的数目
    void backtracking(int n, string path, vector<string> &result, int l, int r) {
        if (l == n && r == n) {
            result.push_back(path);
            return;
        }

        if (l < n) {
            backtracking(n, path+"(", result, l+1, r);
        }

        if (r < l) {
            backtracking(n, path+")", result, l, r+1);
        }
    }
};
