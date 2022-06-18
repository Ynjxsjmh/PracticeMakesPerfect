# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: house-robber-iii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-17 14:18:35
# Last Updated:
#           By: Ynjxsjmh
# Description: The thief has found himself a new place for his
# thievery again. There is only one entrance to this area, called
# `root`.

# Besides the `root`, each house has one and only one parent
# house. After a tour, the smart thief realized that all houses in this
# place form a binary tree. It will automatically contact the police if
# **two directly-linked houses were broken into on the same night**.
#
# Given the `root` of the binary tree, return *the maximum amount of
# money the thief can rob **without alerting the police***.
#
# Example 1:
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
# Example 2:
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
# Constraints:
# *   The number of nodes in the tree is in the range `[1, 104]`.
# *   `0 <= Node.val <= 104`
# ********************************************************************************


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        We construct a dp tree.
        Each node (dp_node) in this dp tree is an array of two elements:
        dp_node = [your gain when you ROB the current node,
                   your gain when you SKIP the current node]
        -  dp_node[0] =[your gain when you ROB the current node]
        -  dp_node[1] =[your gain when you SKIP the current node]

        we start by scanning from the leaf: Depth First Search

        For each node you have 2 options:

        option 1: ROB the node, then you can't rob the child/children of the node.
                  dp_node[0] = node.val + dp_node.left[1] + dp_node.right[1]
        option 2: SKIP the node, then you can ROB or SKIP the child/children of the node.
                  dp_node[1] = max(dp_node.left[0], dp_node.left[1]) +
                               max(dp_node.right[0], dp_node.right[1])

        The maximum of gain of the node depends on max(dp_node[0],dp_node[1])

        :type root: TreeNode
        :rtype: int
        """

        return max(self.dfs(root))

    def dfs(self, node):
        if not node:
            return (0, 0)

        left  = self.dfs(node.left)
        right = self.dfs(node.right)

        return (
            # ROB current node
            node.val + left[1] + right[1],
            # SKIP current node
            # ROB or SKIP the child node
            max(left[0], left[1]) + max(right[0], right[1])
        )
