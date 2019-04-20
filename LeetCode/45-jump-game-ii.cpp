#include <vector>
#include <iostream>
using namespace std;

int jump(vector<int>& nums) {
    int jumpNum = 0;
    int curEnd = 0;
    int curFarthest = 0;

    for (int i = 0; i < nums.size()-1; i++) {
        curFarthest = max(curFarthest, i+nums[i]);
        if (i == curEnd) {
            jumpNum++;
            curEnd = curFarthest;
        }
    }

    return jumpNum;
}