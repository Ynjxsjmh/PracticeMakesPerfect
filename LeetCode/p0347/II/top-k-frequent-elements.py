# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: top-k-frequent-elements.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-07 16:08:00
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an integer array `nums` and an integer `k`,
# return *the* `k` *most frequent elements*. You may return the answer
# in **any order**.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# *   `1 <= nums.length <= 105`
# *   `-104 <= nums[i] <= 104`
# *   `k` is in the range `[1, the number of unique elements in the array]`.
# *   It is **guaranteed** that the answer is **unique**.
#
# **Follow up:** Your algorithm's time complexity must be better than
# **`O(n log n)`, where n is the array's size.
# ********************************************************************************



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # num -> frequency
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Python 默认是小根堆，取相反数的话当成大根堆
        # v 值越大，-v 就越小
        max_heap = [(-v, num) for num, v in freq.items()]
        heapq.heapify(max_heap)

        # 根是最小的 -v，即最大的 v
        # 循环弹出 k 个最大的 v
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res
