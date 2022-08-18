# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: binary-tree-level-order-traversal.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-10 03:38:24
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, return *the level
# order traversal of its nodes' values*. (i.e., from left to right,
# level by level).
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []
        curr_level = [root]

        while len(curr_level):
            next_level = []
            curr_level_val = []

            for node in curr_level:
                curr_level_val.append(node.val)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            res.append(curr_level_val)
            curr_level = next_level

        return res
