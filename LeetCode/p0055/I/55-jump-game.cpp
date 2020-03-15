#include <vector>
#include <iostream>
using namespace std;

bool canJump(vector<int>& nums) {
    int possible = nums.size()-1;

    for (int i = nums.size()-2; i >= 0; i--) {
        if (nums[i] >= nums.size() - 1 - i || nums[i] >= possible - i) {
            possible = i;
        }
    }

    return possible == 0 ? true : false;
}

/* 超时
bool canJump(vector<int>& nums) {
    return jump(nums, 0);
}

bool jump(vector<int>& nums, int start) {
    if (nums[start] >= nums.size() - start - 1) {
        return true;
    }

    bool result = false;

    for (int i = start+1; i < (start+nums[start]+1) && i < nums.size(); i++) {
        result = result or jump(nums, i);
        if (result) {
            return true;
        }
    }

    return result;
}
*/