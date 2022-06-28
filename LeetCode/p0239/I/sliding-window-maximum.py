# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: sliding-window-maximum.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-28 10:03:33
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an array of integers `nums`, there is a
# sliding window of size `k` which is moving from the very left of the
# array to the very right. You can only see the `k` numbers in the
# window. Each time the sliding window moves right by one position.
#
# Return *the max sliding window*.
#
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# *   `1 <= nums.length <= 105`
# *   `-104 <= nums[i] <= 104`
# *   `1 <= k <= nums.length`
# ********************************************************************************


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """使用大根堆记录滑动窗口内 k 个数和索引，
        因此根节点就是窗口内的最大数和其索引。
        每次窗口右移时，当新数加进堆中，
        1. 新数是最大的，直接取堆顶
        2. 新数不是最大的，比较堆顶索引是否在当前
           滑动窗口内，不是的话弹出，直到堆顶索引
           在滑动窗口内。此时堆顶为窗口内最大值。
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)

        max_nums = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i-k:
                heapq.heappop(heap)

            max_nums.append(-heap[0][0])

        return max_nums
