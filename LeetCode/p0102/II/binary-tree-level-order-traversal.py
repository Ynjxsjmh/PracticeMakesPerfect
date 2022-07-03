# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: binary-tree-level-order-traversal.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-03 10:53:05
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
        """简单的二叉树迭代层次遍历
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

        return res
