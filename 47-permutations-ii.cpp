#include <vector>
#include <iostream>
using namespace std;

void permutation(vector<int> nums, vector<vector<int> >& result, vector<int>& tempResult) {
    if (nums.size() <= 0) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = 0; i < nums.size(); i++) {
        vector<int> tempNums(nums);
        tempResult.push_back(nums[i]);
        tempNums.erase(tempNums.begin()+i);
        permutation(tempNums, result, tempResult);
        tempResult.pop_back();
    }
}

vector<vector<int> > permuteUnique(vector<int>& nums) {
    vector<vector<int> > result;
    vector<int> tempResult;

    permutation(nums, result, tempResult);

    // 去除返回的 result 重复的，但超时
    for (int i = 0; i < result.size(); i++) {
        for (int j = i+1; j < result.size(); j++) {
            bool flag = true;
            for (int k = 0; k < nums.size(); k++) {
                flag = flag and (result[i][k] == result[j][k]);
            }
            if (flag) {
                result.erase(result.begin()+j);
                j--; // 当移除和 i 重复的元素后，result 的元素从 j 开始前移。此时 j 应该保持不变，因此是 j-- 和循环的 ++ 抵消
            }
        }
    }

    return result;
}



vector<vector<int> > permuteUnique2(vector<int> &num) {
    vector<vector<int>> result;
    vector<int> tempResult;
    map<int, int> map;
    for (int i : num)
    {
        // 记录 nums 中每个数字的出现次数。
        if (map.find(i) == map.end()) map[i] = 0;
        map[i]++;
    }
    permuteUnique2(result, tempResult, map, num.size());
    return result;
}

void permuteUnique2(vector<vector<int>> &result, vector<int> &tempResult, map<int, int> &map, int n)
{
    if (n <= 0)
    {
        result.push_back(tempResult);
        return;
    }
    for (auto &p : map)
    {
        if (p.second <= 0) continue;
        p.second--;
        tempResult.push_back(p.first);
        permuteUnique2(result, tempResult, map, n - 1);
        tempResult.pop_back();
        p.second++;
    }
}