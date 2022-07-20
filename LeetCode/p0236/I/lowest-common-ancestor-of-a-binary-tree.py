# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: lowest-common-ancestor-of-a-binary-tree.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-20 23:38:05
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given a binary tree, find the lowest common ancestor
# (LCA) of two given nodes in the tree.
#
# According to the [definition of LCA on
# Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):
# “The lowest common ancestor is defined between two nodes `p` and `q`
# as the lowest node in `T` that has both `p` and `q` as descendants
# (where we allow **a node to be a descendant of itself**).”
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.
#
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
# Constraints:
# *   The number of nodes in the tree is in the range `[2, 105]`.
# *   `-109 <= Node.val <= 109`
# *   All `Node.val` are **unique**.
# *   `p != q`
# *   `p` and `q` will exist in the tree.
# ********************************************************************************



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.parent = {root.val: None}
        self.dfs(root)

        p_parent = [p.val]
        while self.parent[p.val] != None:
            p.val = self.parent[p.val]
            p_parent.append(p.val)

        while q.val not in p_parent:
            q.val = self.parent[q.val]

        return TreeNode(q.val)


    def dfs(self, root):
        if not root:
            return

        if root.left:
            self.parent[root.left.val] = root.val
            self.dfs(root.left)

        if root.right:
            self.parent[root.right.val] = root.val
            self.dfs(root.right)