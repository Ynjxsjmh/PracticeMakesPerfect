#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] > nums[l]) {
                // 左边数组有序，递增
                if (nums[mid-1] >= target && nums[l] <= target) { // target 在左边
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                // 右边数组有序，递增
                if (nums[mid+1] <= target && nums[r] >= target) { // target 在右边
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
};