# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: kth-largest-element-in-an-array.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-10 13:38:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and an integer `k`,
# return *the* `kth` *largest element in the array*.
#
# Note that it is the `kth` largest element in the sorted order, not
# the `kth` distinct element.
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
# *   `1 <= k <= nums.length <= 104`
# *   `-104 <= nums[i] <= 104`
# ********************************************************************************


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap))

        return -res[-1]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []

        for i in range(k):
            heapq.heappush(heap, nums[i])

        # 堆内维护 k 个元素，特点为过去最大的
        # 因为为小根堆，因此根就是 k 个最大里最小的，
        # 即第 K 个最大元素
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

        return heap[0]
