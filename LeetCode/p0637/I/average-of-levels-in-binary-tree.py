# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: average-of-levels-in-binary-tree.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-06 10:43:02
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, return *the average
# value of the nodes on each level in the form of an array*. Answers
# within `10-5` of the actual answer will be accepted.
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is
# 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
# Constraints:
# *   The number of nodes in the tree is in the range `[1, 104]`.
# *   `-231 <= Node.val <= 231 - 1`
# ********************************************************************************


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """二叉树层次遍历
        :type root: TreeNode
        :rtype: List[float]
        """

        res = []
        q = deque()
        q.append(root)

        while q:
            cur_level_num = len(q)
            cur_level_sum = 0

            for _ in range(cur_level_num):
                cur_node = q.popleft()
                cur_level_sum += cur_node.val

                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)

            res.append(float(cur_level_sum)/cur_level_num)

        return res
