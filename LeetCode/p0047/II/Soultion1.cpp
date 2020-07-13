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
 * @since  2020-07-13 16:24
 * @tag    backtracking
 * @repeat
 */


class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int> > result;
        vector<int> tempResult;
        vector<int> used(nums.size());

        std::sort(nums.begin(), nums.end());
        dfs(nums, tempResult, result, used);

        return result;
    }

    void dfs(vector<int>& nums, vector<int>& tempResult, vector<vector<int> >& result, vector<int>& used) {
        if (tempResult.size() >= nums.size()) {
            result.push_back(tempResult);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (used[i] || i > 0 && nums[i] == nums[i-1] && !used[i-1]) {
                continue;
            }

            used[i] = 1;
            tempResult.push_back(nums[i]);
            dfs(nums, tempResult, result, used);
            used[i] = 0;
            tempResult.pop_back();
        }
    }
};
