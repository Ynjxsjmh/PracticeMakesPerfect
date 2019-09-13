#include <vector>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

		vector<vector<int>> result;

        if(nums.size()<3)
            return result;

        for (int i = 0; i < nums.size()-2; i++) {
            int l = i+1;
            int r = nums.size()-1;

            while (l<r) {
				if(i>0 && nums[i]==nums[i-1]) continue;

                int threeSum = nums.at(i) + nums.at(l) + nums.at(r);
                if (threeSum == 0) {
                    result.push_back({nums.at(i), nums.at(l), nums.at(r)});
                    l++; r--;
                    while (l<r && nums.at(l)==nums.at(l-1)) l++;
                    while (l<r && nums.at(r)==nums.at(r+1)) r--;
                } else if (threeSum < 0) {
                    l++;
                    while(l<r && nums[l]==nums[l-1])l++;
                } else {
                    r--;
                    while(l<r && nums[r]==nums[r+1])r--;
                }
            }
        }
		return result;
    }
};