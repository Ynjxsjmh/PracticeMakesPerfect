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
 * @since  2020-07-13 22:03
 * @tag    backtracking
 * @repeat
 */

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string> > result;
        vector<string> tempResult;

        dfs(s, 0, tempResult, result);

        return result;
    }

    void dfs(string s, int left, vector<string>& tempResult, vector<vector<string> >& result) {
        if (left >= s.size()) {
            result.push_back(tempResult);
            return;
        }

        for (int i = left; i < s.size(); i++) {
            if (isPalidrome(s, left, i)) {
                tempResult.push_back(s.substr(left, i-left+1));
                dfs(s, i+1, tempResult, result);
                tempResult.pop_back();
            }
        }
    }

    bool isPalidrome(string s, int left, int right) {
        while (left < right) {
            if (s[left++] != s[right--]) {
                return false;
            }
        }

        return true;
    }
};
