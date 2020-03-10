/**
 * Description
 * Given an array `nums` of n integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
 *
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-03-11 02:44
 * @tag
 * @repeat
 */

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int> > fresult;

        int length = nums.size();
        for (int i = 0; i < length-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) // avoid duplicate
                continue ;

            int j = i + 1;
            int k = length - 1;
            int target = 0 - nums[i];

            while (j < k) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    // avoid duplicate
                    j++;
                    continue ;
                }

                int sum = nums[j] + nums[k];

                if (sum == target) {
                    vector<int> result;
                    result.push_back(nums[i]);
                    result.push_back(nums[j++]);
                    result.push_back(nums[k--]);
                    fresult.push_back(result);
                } else if (sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return fresult;
    }
};
