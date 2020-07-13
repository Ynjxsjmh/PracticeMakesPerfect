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
 * @since  2020-07-13 21:10
 * @tag    backtracking
 * @repeat
 */

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int> > result;
        vector<int> tempResult;

        std::sort(candidates.begin(), candidates.end());

        dfs(candidates, 0, target, tempResult, result);

        return result;
    }

    void dfs(vector<int>& candidates, int left, int remain, vector<int>& tempResult, vector<vector<int> >& result) {
        if (remain < 0) {
            return;
        }

        if (remain == 0) {
            result.push_back(tempResult);
            return;
        }

        for (int i = left; i < candidates.size(); i++) {
            if (i > left && candidates[i] == candidates[i-1]) continue;

            tempResult.push_back(candidates[i]);
            dfs(candidates, i + 1, remain - candidates[i], tempResult, result);
            tempResult.pop_back();
        }
    }
};
