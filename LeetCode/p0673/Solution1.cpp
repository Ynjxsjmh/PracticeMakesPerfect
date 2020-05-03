/**
 * Description
 *
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-05-03 15:04
 * @tag    DP
 * @repeat
 */



class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();

        if (n <= 0) {
            return 0;
        }

        vector<int> len(n, 1);
        vector<int> cnt(n, 1);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    if (len[i] == len[j] + 1) {
                        cnt[i] += cnt[j];
                    }

                    if (len[i] < len[j] + 1) {
                        len[i] = len[j] + 1;
                        cnt[i] = cnt[j];
                    }
                }
            }
        }

        int longest = *max_element(len.begin(), len.end());
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (len[i] == longest) {
                res += cnt[i];
            }
        }

        return res;
    }

};
