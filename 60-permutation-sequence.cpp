#include <vector>
#include <iostream>
using namespace std;

string getPermutation(int n, int k) {
    vector<int> nums;
    vector<int> tempResult;
    vector<vector<int> > result;
    string ans;

    for (int i = 1; i <= n; i++) {
        nums.push_back(i);
    }

    permutation(nums, result, tempResult);

    for (int i = 0; i < result[k-1].size(); i++) {
        ans += to_string(result[k-1][i]);
    }

    return ans;
}

void permutation(vector<int> nums, vector<vector<int> >& result, vector<int>& tempResult) {
    if (nums.size() == tempResult.size()) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (find(tempResult.begin(), tempResult.end(), nums[i]) != tempResult.end()) {
            continue;
        }

        tempResult.push_back(nums[i]);
        permutation(nums, result, tempResult);
        tempResult.pop_back();
    }
}

string getPermutation2(int n, int k) {
    /* 1-n 个数的排列：
     * 以 1 开头的有 (n-1)! 这么多
     * 以 2 开头的有 (n-1)! 这么多
     *
     * 如果 k 小于 (n-1)!，那么 k 一定以 1 开头
     * 由于数字不能重复，因此又有
     * 以 12 开头的有 (n-2)! 这么多
     * 以 13 开头的有 (n-2)! 这么多
     * 以此类推，当 n 为 0 时就搞完了
     */

    string result;
    int arr[10] = {1};
    vector<int> nums;

    for (int i = 1; i < 10; i++) {
        arr[i] = i * arr[i-1];  // 记录 n 的阶乘
        nums.push_back(i);
    }

    while (n) {
        int temp = (k-1) / arr[n-1];  // 如果 k 刚好为 arr[n-1] 的整数倍，应该属于上一类的最后一个，不能为该整数，故应减一
        result += to_string(nums[temp]);
        nums.erase(nums.begin()+temp);
        k -= temp * arr[n-1];
        n--;
    }

    return result;
}