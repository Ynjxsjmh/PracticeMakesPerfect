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
                // ����������򣬵���
                if (nums[mid-1] >= target && nums[l] <= target) { // target �����
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                // �ұ��������򣬵���
                if (nums[mid+1] <= target && nums[r] >= target) { // target ���ұ�
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
};