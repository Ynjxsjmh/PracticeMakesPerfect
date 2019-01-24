#include <vector>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;

        if(nums.size()<4)
            return result;

        for (int i=0; i<(int)(nums.size()-3); i++) {
            if(i>0 && nums[i]==nums[i-1]) continue;
            for (int j=i+1; j<(int)(nums.size()-2); j++) {
                if(j>i+1 && nums[j]==nums[j-1]) continue;
                int l = j+1;
                int r = nums.size()-1;
                while (l<r) {
                    int tempSum = nums.at(i) + nums.at(j) + nums.at(l) + nums.at(r);
                    if (tempSum == target) {
                        result.push_back({nums.at(i), nums.at(j), nums.at(l), nums.at(r)});
                        l++; r--;
                        while(l<r && nums[l]==nums[l-1])l++;
                        while(l<r && nums[r]==nums[r+1])r--;
                    } else if (tempSum < target) {
                        l++;
                        while(l<r && nums[l]==nums[l-1])l++;
                    } else {
                        r--;
                        while(l<r && nums[r]==nums[r+1])r--;
                    }
                }
            }
        }
        return result;
    }
};

int main() {
    Solution* solution = new Solution;
    vector<int> nums = {};
    int target = 0;
    vector<vector<int>> result = solution->fourSum(nums, target);
    vector<vector<int>>::iterator row;
    vector<int>::iterator col;
    for (row = result.begin(); row != result.end(); row++) {
        for (col = row->begin(); col != row->end(); col++) {
            cout<<*col<<" ";
        }
        cout<<endl;
    }
}