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
 * @since  2020-04-30 14:34
 * @tag    DFS
 * @repeat
 */


class Solution {
public:
    // '0','1','2',...
    const vector<string> keyboard { " ", "", "abc", "def",
            "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

    vector<string> letterCombinations(string digits) {

        if (digits.empty()) return {};
        vector<string> result;

        dfs(digits, 0, "", result);

        return result;
    }

    void dfs(const string &digits, size_t cur, string path, vector<string> &result) {
        if (cur >= digits.size()) {
            result.push_back(path);
            return;
        }

        for (auto ch : keyboard[digits[cur]-'0']) {
            dfs(digits, cur+1, path+ch, result);
        }
    }
};