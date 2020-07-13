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
 * @since  2020-07-13 21:27
 * @tag    backtracking
 * @repeat
 */

class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int> > result;
        vector<int> tempResult;

        dfs(n, k, 1, tempResult, result);

        return result;
    }

    void dfs(int remain, int k, int left, vector<int>& tempResult, vector<vector<int> >& result) {
        if (remain < 0) {
            return;
        }

        if (remain == 0 && k == 0) {
            result.push_back(tempResult);
            return;
        }

        for (int i = left; i <= 9; i++) {
            tempResult.push_back(i);
            dfs(remain - i, k - 1, i + 1, tempResult, result);
            tempResult.pop_back();
        }
    }
};
