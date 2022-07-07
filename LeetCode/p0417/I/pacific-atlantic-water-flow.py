# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: pacific-atlantic-water-flow.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-07 00:43:38
# Last Updated: 
#           By: Ynjxsjmh
# Description: There is an `m x n` rectangular island that borders
# both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific
# Ocean** touches the island's left and top edges, and the **Atlantic
# Ocean** touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given
# an `m x n` integer matrix `heights` where `heights[r][c]` represents
# the **height above sea level** of the cell at coordinate `(r, c)`.
#
# The island receives a lot of rain, and the rain water can flow to
# neighboring cells directly north, south, east, and west if the
# neighboring cell's height is **less than or equal to** the current
# cell's height. Water can flow from any cell adjacent to an ocean
# into the ocean.
#
# Return *a **2D list** of grid coordinates* `result` *where*
# `result[i] = [ri, ci]` *denotes that rain water can flow from cell*
# `(ri, ci)` *to **both** the Pacific and Atlantic oceans*.
#
# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
# Constraints:
# *   `m == heights.length`
# *   `n == heights[r].length`
# *   `1 <= m, n <= 200`
# *   `0 <= heights[r][c] <= 105`
# ********************************************************************************


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        self.m, self.n = len(heights), len(heights[0])

        # 四条边是一开始能流入 pacific 或 atlantic 的坐标
        pacific = [(r, 0) for r in range(self.m)] + [(0, c) for c in range(1, self.n)]
        atlantic = [(r, self.n-1) for r in range(self.m)] + [(self.m-1, c) for c in range(self.n-1)]

        return list(map(list, self.bfs(pacific, heights) & self.bfs(atlantic, heights)))

    def bfs(self, starts, heights):
        q = deque(starts)
        visited = set(starts)

        while q:
            x, y = q.popleft()

            # 上下左右判断是否能够回流
            for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                if 0 <= nx < self.m and 0 <= ny < self.n \
                   and heights[nx][ny] >= heights[x][y] \
                   and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))

        return visited
