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
 * @since  2020-07-12 18:31
 * @tag    backtracking
 * @repeat
 */


class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int> > result;
        vector<int> tempResult;
        sort(nums.begin(), nums.end());

        dfs(nums, 0, tempResult, result);

        return result;
    }

    void dfs(vector<int>& nums, int start, vector<int>& tempResult, vector<vector<int> >& result) {
        result.push_back(tempResult);

        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            tempResult.push_back(nums[i]);
            dfs(nums, i+1, tempResult, result);
            tempResult.pop_back();
        }
    }
};
