# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: two-sum-iv-input-is-a-bst.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-09 23:48:10
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
    def findTarget(self, root, k):
        """类似 Two Sum, 遍历树时存 map
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        lst = []
        return self.dfs(root, k, lst)

    def dfs(self, node, k, lst):
        if node == None:
            return False

        if node.val in lst:
            return True
        else:
            lst.append(k - node.val)
            return self.dfs(node.left, k, lst) | self.dfs(node.right, k, lst)
