/*********************************************************************************
 Copyright © 2020 Ynjxsjmh
 File Name: Solution1.cpp
 Author: Ynjxsjmh
 Email: ynjxsjmh@gmail.com
 Created: 2020-07-12 09:34:35
 Last Updated: 
           By: Ynjxsjmh
 Description: 
 *********************************************************************************/
#include<cstdio>
#include<cstring>

vector<vector<int> > subsets(vector<int>& nums) {
    vector<vector<int> > result;
    vector<int> tempResult;
    dfs(0, tempResult, nums, result);
    return result;
}

void dfs(int left, vector<int>& tempResult, vector<int>& nums, vector<vector<int> >& result) {
    result.push_back(tempResult);

    for (int i = left; i < nums.size(); i++) {
        tempResult.push_back(nums[i]);
        dfs(i+1, tempResult, nums, result);
        tempResult.pop_back();
    }
}
