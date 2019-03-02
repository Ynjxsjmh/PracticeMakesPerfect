vector<vector<int>> combinationSum(vector<int>& candidates, int target)
{
    vector<vector<int>> result;
    vector<int> tempResult;
    sort(candidates.begin(), candidates.end());
    combination(candidates, target, tempResult, result, 0);

    return result;
}

void combination(vector<int>& candidates, int target, vector<int>& tempResult, vector<vector<int>>& result, int begin)
{
    if (target == 0)
    {
        result.push_back(tempResult);
        return ;
    }

    for (int i = begin; i < candidates.size(); i++) {
        if (candidates[i] <= target) {
            tempResult.push_back(candidates[i]);
            combination(candidates, target-candidates[i], tempResult, result, i);
            tempResult.pop_back();
        }
    }
}