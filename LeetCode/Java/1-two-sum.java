/**
 * Description
 * Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.
 *
 * You may assume that each input would have **exactly** one solution, and you may not use the same element twice.
 *
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-02-23 02:13
 * @tag    Array, Hash Table
 */

class Solution {
    /**
     * Approach 1: Brute Force
     * Time complexity: O(n^2)
     * Space complexity : O(1)
     */
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i<nums.length; i++) {
            for (int j=i+1; j<nums.length; j++) {
                if (nums[i]+nums[j]==target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0, 0};
    }
}



// What is the best way to maintain a mapping of each element in the array to its index? A hash table.

class Solution {
    // Approach 2: Two-pass Hash Table
    // Time complexity : O(n)
    // Space complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int result = target - nums[i];
            if (map.containsKey(result) && map.get(result) != i) {
                // 后一个判断条件：Given nums = [3,2,4], target = 6
                return new int[] {i, map.get(result)};
            }
        }

        return new int[] {0, 0};
    }
}


