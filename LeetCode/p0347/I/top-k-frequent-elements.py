# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: top-k-frequent-elements.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-09 16:10:03
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
# *   `k` is in the range `[1, the number of unique elements in the array]`.
# *   It is **guaranteed** that the answer is **unique**.
# ********************************************************************************


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = defaultdict(lambda: 0)

        for num in nums:
            freq[num] += 1

        return list(reversed(sorted(freq.keys(), key=lambda k: freq[k])))[:k]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = defaultdict(lambda: 0)

        for num in nums:
            freq[num] += 1

        max_heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(max_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
