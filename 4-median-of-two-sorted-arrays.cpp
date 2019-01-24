#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> sortedArray;
        int i=0;
        int j=0;
        int k=0;
        while(i<nums1.size() && j<nums2.size()) {
            if (nums1[i]<=nums2[j]) {
                sortedArray.push_back(nums1[i]);
                i++;
            } else {
                sortedArray.push_back(nums2[j]);
                j++;
            }
        }

        while (i<nums1.size()) {
            sortedArray.push_back(nums1[i]);
            i++;
        }

        while (j<nums2.size()) {
            sortedArray.push_back(nums2[j]);
            j++;
        }

        int len = nums1.size() + nums2.size();
        int index = 0;
        if (len%2) {
            // 如果是奇数
            index = (len+1)/2;
            return sortedArray.at(index-1);
        } else {
            index = len/2;
            return (double)(sortedArray.at(index-1)+sortedArray.at(index))/2;
        }
    }
};

int main() {
    Solution* solution = new Solution;
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {3, 4};
    cout<< solution->findMedianSortedArrays(nums1, nums2) <<endl;
}