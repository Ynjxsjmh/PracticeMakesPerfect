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
 * @since  2020-07-13 15:37
 * @tag    backtracking
 * @repeat
 */

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > result;
        vector<int> tempResult;

        dfs(nums, tempResult, result);

        return result;
    }

    void dfs(vector<int>& nums, vector<int>& tempResult, vector<vector<int> >& result) {
        if (tempResult.size() >= nums.size()) {
            result.push_back(tempResult);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (std::find(tempResult.begin(), tempResult.end(), nums[i]) != tempResult.end()) {
                continue;
            }

            tempResult.push_back(nums[i]);
            dfs(nums, tempResult, result);
            tempResult.pop_back();
        }
    }
};
