# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: binary-tree-right-side-view.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-07 00:38:12
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, imagine yourself
# standing on the **right side** of it, return *the values of the
# nodes you can see ordered from top to bottom*.
#
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]
#
# Example 3:
# Input: root = []
# Output: []
#
# Constraints:
# *   The number of nodes in the tree is in the range `[0, 100]`.
# *   `-100 <= Node.val <= 100`
# ********************************************************************************


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """二叉树层次遍历，每层的最后一个节点
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return None

        q = deque()
        q.append(root)
        res = []

        while q:
            cur_level_num = len(q)

            for _ in range(cur_level_num):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            res.append(cur.val)

        return res
