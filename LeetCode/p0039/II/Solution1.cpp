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
 * @since  2020-07-13 20:33
 * @tag    backtracking
 * @repeat
 */



class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > result;
        vector<int> tempResult;

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
            tempResult.push_back(candidates[i]);
            dfs(candidates, i, remain - candidates[i], tempResult, result);
            tempResult.pop_back();
        }
    }
};