# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: course-schedule.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-03 14:41:33
# Last Updated: 
#           By: Ynjxsjmh
# Description: There are a total of `numCourses` courses you have to
# take, labeled from `0` to `numCourses - 1`. You are given an array
# `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that
# you **must** take course `bi` first if you want to take course `ai`.
#
# *   For example, the pair `[0, 1]`, indicates that to take course
# *   `0` you have to first take course `1`.
#
# Return `true` if you can finish all courses. Otherwise, return `false`.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take
# course 0 you should also have finished course 1. So it is
# impossible.
#
# Constraints:
# *   `1 <= numCourses <= 2000`
# *   `0 <= prerequisites.length <= 5000`
# *   `prerequisites[i].length == 2`
# *   `0 <= ai, bi < numCourses`
# *   All the pairs prerequisites[i] are **unique**.
# ********************************************************************************


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """有向无环图
        1. 生成入度表
        2. 用邻接表建图
        3. bfs 拓扑排序
           3.1 统计入度为 0 的节点
           3.2 从图中依次删除入度为 0 的节点，
               同时将其子节点的入度减一
           3.3 重复 3.1, 3.2
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        queue = deque()

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            numCourses -= 1

            for adj in adjacency[cur]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        return numCourses == 0
