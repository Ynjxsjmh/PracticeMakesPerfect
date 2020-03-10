/**
 * Description
 *
 *
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-03-11 02:52
 * @tag
 * @repeat
 */

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int len = nums.size();
        int distance = INT_MAX;
        int sum;

        for (int i = 0; i < nums.size(); i++) {
            cout << nums[i] << " ";
        }

        for (int i = 0; i < len-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int j = i + 1;
            int k = len - 1;

            while (j < k) {
                int cur_sum = nums[i] + nums[j] + nums[k];
                int cur_dis = target - cur_sum;

                if (j > i+1 && nums[j] == nums[j-1]) {
                    j++;
                    continue;
                }

                if (cur_sum == target) {
                    return target;
                } else if (cur_sum < target) {
                    if (abs(cur_dis) < abs(distance)) {
                        distance = cur_dis;
                        sum = cur_sum;
                    }
                    j++;
                } else {
                    if (abs(cur_dis) < abs(distance)) {
                        distance = cur_dis;
                        sum = cur_sum;
                    }
                    k--;
                }
            }
        }

        return sum;
    }
};
