# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: minimum-height-trees.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-21 13:09:13
# Last Updated: 
#           By: Ynjxsjmh
# Description: A tree is an undirected graph in which any two vertices
# are connected by *exactly* one path. In other words, any connected
# graph without simple cycles is a tree.
#
# Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array
# of `n - 1` `edges` where `edges[i] = [ai, bi]` indicates that there
# is an undirected edge between the two nodes `ai` and `bi` in the
# tree, you can choose any node of the tree as the root. When you
# select a node `x` as the root, the result tree has height `h`. Among
# all possible rooted trees, those with minimum height
# (i.e. `min(h)`)  are called **minimum height trees** (MHTs).
#
# Return *a list of all **MHTs'** root labels*. You can return the answer in **any order**.
#
# The **height** of a rooted tree is the number of edges on the
# longest downward path between the root and a leaf.
#
# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is
# the node with label 1 which is the only MHT.
#
# Example 2:
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
#
# Constraints:
# *   `1 <= n <= 2 * 104`
# *   `edges.length == n - 1`
# *   `0 <= ai, bi < n`
# *   `ai != bi`
# *   All the pairs `(ai, bi)` are distinct.
# *   The given input is **guaranteed** to be a tree and there will be **no repeated** edges.
# ********************************************************************************



class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        u 为根
              a1\      /b1
              a2-u----v-b2
              a3/      \b3
        先计算在 u 为根的树中，以各节点为根的子树高度
        height_u[u] 表示“在 u 为根的树中，以 u 为根的子树高度”，即树高
        height_u[v] 表示“在 u 为根的树中，以 v 为根的子树高度”

        u 换根成 v，我们想求以 v 为根的树高
              a1\ 换根 /b1
              a2-u----v-b2
              a3/      \b3
        height[v] = height_v[v] = max(height_u[v], height_v[u]+1)
        height_v[u] 的高度怎么求呢？我们注意到：
          以 a1-a3, b1-b3 为根的子树高度都保持不变，
          对这些节点来说其 height_v 就等于 height_u
        1. height_v[u] 可以通过求 a1-a3 的最大值来求得

        2. height_v[u] 还可以通过记录在 以 u 为根的树中，a1-a3 和 v 为根的子树高度最大值和次大值
          - 如果v 为根的子树高度是最大的，a1-a3 的值中只有次大值
          - 如果v 为根的子树高度不是最大的，a1-a3 的值中还有最大值
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.graph = [[] for _ in range(n)]

        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        # 在以 0 号节点为根的树中，以各节点为根的子树高度
        self.height0 = [0] * n
        # 以各个节点为根的树高
        self.height  = [0] * n

        self.dfs0(0)
        self.dfs1(0)

        h = n
        ans = []

        # 找 self.height 所有最小值
        for i in range(n):
            if self.height[i] < h:
                h = self.height[i]
                ans = []

            if self.height[i] == h:
                ans.append(i)

        return ans

    def dfs0(self, u):
        '''在以 0 号节点为根的树中，根为 u 节点的子树高度
        '''

        # 1. 一开始只在根为 u 节点的子树看到 u
        #    因此高度初始化为 1
        # 2. self.dfs0(v) 时，遍历会看到 u，
        #    需要标记 u 节点是父节点，
        self.height0[u] = 1
        h = 0

        # 遍历根节点 u 的所有邻接节点 v
        for v in self.graph[u]:
            # 如果 height0[v] 已经计算过了
            # 说明邻接节点 v 是 u 的父节点
            if self.height0[v] != 0:
                continue

            # 计算 u 的所有子节点的高度，取最大值
            self.dfs0(v)
            h = max(h, self.height0[v])

        self.height0[u] = h + 1

    def dfs1(self, u):
        '''进行换根动态规划，计算出以各节点为根的所有树的高度
        原先以 u 为根，换成以 v 为根，其中 v 为 u 的某个子节点
        self.height0 的含义 self.height_u，即以 u 为根的树
        '''

        # 记录以 u 为根的树的高度的最大值和次大值
        # 便于在换根成 v 时，重新计算以 u 为根的子树的高度
        first, second = 0, 0

        for v in self.graph[u]:
            if self.height0[v] > first:
                second = first
                first = self.height0[v]

            elif self.height0[v] > second:
                second = self.height0[v]

        # 遍历 u 的邻接节点
        for v in self.graph[u]:
            # 如果 v 节点的高度计算过
            # 说明 v 是 u 的父节点
            if self.height[v] != 0:
                continue

            # 将 u 和子节点 v 进行换根
            # 先计算在以 v 为根的树中，以 u 为根的子树高度
            self.height0[u] = (first if self.height0[v] != first else second) + 1
            # 计算以 v 为根的树高
            self.height[v] = max(self.height0[v], self.height0[u] + 1);
            self.dfs1(v)
