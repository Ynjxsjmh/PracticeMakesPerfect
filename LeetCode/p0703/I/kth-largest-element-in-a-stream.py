# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: kth-largest-element-in-a-stream.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-09 21:34:08
# Last Updated:
#           By: Ynjxsjmh
# Description: Design a class to find the `kth` largest element in a
# stream. Note that it is the `kth` largest element in the sorted
# order, not the `kth` distinct element.
#
# Implement `KthLargest` class:
# *   `KthLargest(int k, int[] nums)` Initializes the object with the
#     integer `k` and the stream of integers `nums`.
# *   `int add(int val)` Appends the integer `val` to the stream and
#     returns the element representing the `kth` largest element in
#     the stream.
#
# **Example 1:**
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#
# Constraints:
# *   `1 <= k <= 104`
# *   `0 <= nums.length <= 104`
# *   `-104 <= nums[i] <= 104`
# *   `-104 <= val <= 104`
# *   At most `104` calls will be made to `add`.
# *   It is guaranteed that there will be at least `k` elements in the array when you search for the `kth` element.
# ********************************************************************************



class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.nums = []
        self.max_len = k

        for num in nums:
            heapq.heappush(self.nums, num)
            if len(self.nums) > self.max_len:
                heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.nums, val)
        if len(self.nums) > self.max_len:
            heapq.heappop(self.nums)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
