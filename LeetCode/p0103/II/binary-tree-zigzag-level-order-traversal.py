# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: binary-tree-zigzag-level-order-traversal.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-03 13:36:52
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, return *the zigzag
# level order traversal of its nodes' values*. (i.e., from left to
# right, then right to left for the next level and alternate between).
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
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
# *   `-100 <= Node.val <= 100`
# ********************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        cur_level = []
        next_level = [root]
        to_left = True
        res = []

        while next_level:
            cur_level = next_level
            next_level = []
            cur_level_nums = []

            for cur in cur_level:
                if to_left:
                    cur_level_nums.append(cur.val)
                else:
                    cur_level_nums = [cur.val] + cur_level_nums

                if cur.left:
                    next_level.append(cur.left)

                if cur.right:
                    next_level.append(cur.right)

            to_left = not to_left
            res.append(cur_level_nums)

        return res
