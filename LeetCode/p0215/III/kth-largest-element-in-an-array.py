# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: kth-largest-element-in-an-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-06 21:21:54
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and an integer `k`,
# return *the* `kth` *largest element in the array*.
#
# Note that it is the `kth` largest element in the sorted order, not
# the `kth` distinct element.
#
# You must solve it in `O(n)` time complexity.
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
# Constraints:
# *   `1 <= k <= nums.length <= 105`
# *   `-104 <= nums[i] <= 104`
# ********************************************************************************


import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """维护一个大小为 k 的小根堆，
        用于存放数组里的 k 个最大的数，
        由于小根堆根最小，根就是第 k 大的数。

        保证堆里存放是 k 个最大数的方法是，
        每当遇到的新数比堆根（最小数）大时，
        就更新堆。
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []

        for i in range(k):
            heapq.heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

        return heap[0]
