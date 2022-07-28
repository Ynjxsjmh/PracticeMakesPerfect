# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: remove-duplicates-from-sorted-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-27 10:45:40
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` sorted in
# **non-decreasing order**, remove the duplicates
# [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm)
# such that each unique element appears only **once**. The **relative
# order** of the elements should be kept the **same**.
#
# Since it is impossible to change the length of the array in some
# languages, you must instead have the result be placed in the **first
# part** of the array `nums`. More formally, if there are `k` elements
# after removing the duplicates, then the first `k` elements of
# `nums` should hold the final result. It does not matter what you
# leave beyond the first `k` elements.
#
# Return `k` *after placing the final result in the first* `k` *slots
# of* `nums`.
#
# Do **not** allocate extra space for another array. You must do this
# by **modifying the input array
# [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with
# O(1) extra memory.
#
# **Custom Judge:**
#
# The judge will test your solution with the following code:
#
# ```
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums\[i\] == expectedNums\[i\];
# }
# ```
#
# If all assertions pass, then your solution will be **accepted**.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two
# elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they
# are underscores).
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five
# elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they
# are underscores).
#
# Constraints:
# *   `1 <= nums.length <= 3 * 104`
# *   `-100 <= nums[i] <= 100`
# *   `nums` is sorted in **non-decreasing** order.
# ********************************************************************************



class Solution(object):
    def removeDuplicates(self, nums):
        """快慢指针
        由于给定的数组 nums 是有序的，因此对于任意 i<j，
        如果 nums[i]=nums[j]，则对任意 i≤k≤j，必有 nums[i]=nums[k]=nums[j]，
        即相等的元素在数组中的下标一定是连续的。
        利用数组有序的特点，可以通过双指针的方法删除重复元素。

        定义两个指针 fast 和 slow 分别为快指针和慢指针，
        快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置，
        :type nums: List[int]
        :rtype: int
        """

        fast, slow = 1, 0

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                # fast 已经走到下一个数字的第一个
                nums[slow+1] = nums[fast]
                slow += 1
            fast += 1

        return slow + 1
