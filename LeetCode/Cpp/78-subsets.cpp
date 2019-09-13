#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int> > result;
    vector<int> tempResult;

    result.push_back(tempResult);

    for (int i = 1; i < nums.size(); i++) {
        tempResult.clear();
        sub(nums, result, tempResult, i, 0);
    }

    result.push_back(nums);

    return result;
}

void sub(vector<int> nums, vector<vector<int> >& result, vector<int>& tempResult, int n, int begin) {
    if (tempResult.size() == n) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = begin; i < nums.size(); i++) {
        if (find(tempResult.begin(), tempResult.end(), nums[i]) != tempResult.end()) {
            continue;
        }
        tempResult.push_back(nums[i]);
        sub(nums, result, tempResult, n, i); // 这里改成 i+1 更快 XD
        tempResult.pop_back();
    }
}