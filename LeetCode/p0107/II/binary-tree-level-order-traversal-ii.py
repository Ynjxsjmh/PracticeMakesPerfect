# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: binary-tree-level-order-traversal-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-03 13:20:26
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, return *the
# bottom-up level order traversal of its nodes' values*. (i.e., from
# left to right, level by level from leaf to root).
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#
# Example 2:
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
# Input: root = []
# Output: []
#
# Constraints:
# *   The number of nodes in the tree is in the range `[0, 2000]`.
# *   `-1000 <= Node.val <= 1000`
# ********************************************************************************


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """从上到下遍历，然后把结果 reverse 一下
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = deque()
        q.append(root)

        res = []

        while q:
            cur_level_num = len(q)
            cur_level_nums = []

            for _ in range(cur_level_num):
                cur = q.popleft()
                cur_level_nums.append(cur.val)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            res.append(cur_level_nums)

        return res[::-1]

    def levelOrderBottom(self, root):
        """从上到下遍历，存时往前存
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = deque()
        q.append(root)

        res = []

        while q:
            cur_level_num = len(q)
            cur_level_nums = []

            for _ in range(cur_level_num):
                cur = q.popleft()
                cur_level_nums.append(cur.val)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            res = [cur_level_nums] + res

        return res
