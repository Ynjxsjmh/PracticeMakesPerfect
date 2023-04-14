# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: binary-tree-level-order-traversal.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 16:00:00
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
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
        curr_levels = [root]

        while curr_levels:
            next_levels = []
            curr_vals = []
            for node in curr_levels:
                curr_vals.append(node.val)
                if node.left:
                    next_levels.append(node.left)
                if node.right:
                    next_levels.append(node.right)
            curr_levels = next_levels

            res.append(curr_vals)

        return res
