/**
 * Title
 * 923. 3Sum With Multiplicity
 *
 * Description
 * Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
 *
 * As the answer can be very large, return it modulo 10^9 + 7.
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-07-24 10:21
 * @tag
 * @repeat
 */


class Solution {
public:
    int threeSumMulti(vector<int>& A, int target) {
        long count = 0;
        int n = A.size();
        sort(A.begin(), A.end());

        for (int i = 0; i < n; i++) {
            int sum = target - A[i];
            int lo = i + 1, hi = n - 1;

            while (lo < hi) {
                if (A[lo] + A[hi] < sum) {
                    lo++;
                } else if (A[lo] + A[hi] > sum) {
                    hi--;
                } else {
                    int left = 1, right = 1;
                    while (lo + left < hi && A[lo] == A[lo+left]) left++;
                    while (hi - right >= lo + left && A[hi] == A[hi-right]) right++;

                    if (A[lo] != A[hi]) {
                        count += left * right;
                    } else {
                        int n = left + right;
                        count += n * (n - 1) / 2;
                    }

                    lo += left;
                    hi -= right;
                }
            }
        }

        return count % 1000000007;
    }
};
