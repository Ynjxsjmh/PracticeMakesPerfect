#include <algorithm>
#include <iostream>
using namespace std;

int maxSubArray1(vector<int>& nums) {
    // O(n^2)  超时
    int result = nums[0];

    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i; j < nums.size(); ++j) {
            int sum = 0;
            int temp = i;
            while (temp < j) {
                sum += nums[temp];
                temp++;
            }
            result = max(sum, result);
        }
    }

    return result;
}

int maxSubArray(vector<int>& nums) {
    // O(n)
    int result = nums[0];
    int sum = 0;

    for (int i = 0; i < nums.size(); ++i) {
        sum += nums[i];
        result = max(result, sum);
        sum = max(sum, 0);
    }

    return result;
}


int maxSubArray3(vector<int>& nums) {
    // O(nlogn)

    return maxSubArraySum(nums, 0, nums.size()-1);
}

int maxSubArraySum(vector<int>& nums, int l, int r) {
    if (l >= r) {
        return nums[l];
    }

    int m = l + (r-l)/2;

    return max({maxSubArraySum(nums, l, m),
                maxSubArraySum(nums, m+1, r),
                maxCrossingSum(nums, l, m, r)});
}

int maxCrossingSum(vector<int>& nums, int l, int m, int r) {
    int maxLeft = nums[m];
    int maxRight = INT_MIN;
    int sumLeft = 0;
    int sumRight = 0;

    for (int i = m; i >= l; --i) {
        sumLeft += nums[i];
        maxLeft = max(maxLeft, sumLeft);
    }

    for (int i = m+1; i <= r; ++i) {
        sumRight += nums[i];
        maxRight = max(maxRight, sumRight);
    }

    return maxLeft + maxRight;
}