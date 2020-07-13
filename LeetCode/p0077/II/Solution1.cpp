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
 * @since  2020-07-13 19:45
 * @tag    backtracking
 * @repeat
 */

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int> > result;
        vector<int> tempResult;

        dfs(n, k, 1, tempResult, result);

        return result;
    }

    void dfs(int n, int k, int left, vector<int>& tempResult, vector<vector<int> >& result) {
        if (tempResult.size() >= k) {
            result.push_back(tempResult);
            return;
        }

        for (int i = left; i <= n; i++) {
            tempResult.push_back(i);
            dfs(n, k, i+1, tempResult, result);
            tempResult.pop_back();
        }
    }
};
