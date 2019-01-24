#include <vector>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> exsist;
        int index = 0;
        for (int i=0; i<nums.size(); i++) {
            if (exsist.find(nums.at(i)) == exsist.end()) {
                exsist.insert(nums.at(i));
                nums[index] = nums[i];
                index++;
            }
        }
		return exsist.size();
    }
};