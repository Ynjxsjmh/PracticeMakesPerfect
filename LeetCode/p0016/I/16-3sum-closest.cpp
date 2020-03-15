#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <iostream>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int closestNum = nums.at(0)+nums.at(1)+nums.at(2), tempNum = 0; //closestNum 初值不能为 0

        for (int i=0; i<nums.size()-2; i++) {
            int l = i + 1;
            int r = nums.size()-1;

            while (l < r) {
                tempNum = nums.at(i) + nums.at(l) + nums.at(r);

                if (abs(tempNum-target) < abs(closestNum-target)) {
                    closestNum = tempNum;
                }

                if (tempNum < target) {
                    // 此处不能为 l++
                    r--;
                } else if (tempNum > target) {
                    l++;
                } else {
                    return target;
                }
            }
        }

        return closestNum;
    }
};

int main() {
    Solution* solution = new Solution;
    vector<int> nums = {-1, 2, 1, -4};
    int target = 1;
    cout<< solution->threeSumClosest(nums, target);
}
