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
 * @since  2020-04-30 03:18
 * @tag    Two Pointers
 * @repeat
 */

class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = INT_MIN;
        int l = 0;
        int r = height.size() - 1;

        while (l < r) {
            int cur = (r-l)*min(height[l], height[r]);
            result = max(cur, result);

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return result;
    }
};
