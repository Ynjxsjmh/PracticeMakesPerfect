# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: merge-intervals.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-09 01:03:33
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given an array of `intervals` where `intervals[i] =
# [starti, endi]`, merge all overlapping intervals, and return *an
# array of the non-overlapping intervals that cover all the intervals
# in the input*.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Constraints:
# *   `1 <= intervals.length <= 104`
# *   `intervals[i].length == 2`
# *   `0 <= starti <= endi <= 104`
# ********************************************************************************


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key=lambda interval: interval[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            pre_interval = res[-1]
            cur_interval = intervals[i]

            if pre_interval[1] >= cur_interval[0]:
                # 合并
                res = res[:-1]
                res.append([pre_interval[0], max(pre_interval[1], cur_interval[1])])
            else:
                res.append(cur_interval)

        return res
