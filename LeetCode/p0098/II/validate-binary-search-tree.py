# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: validate-binary-search-tree.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-09 10:28:13
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `root` of a binary tree, *determine if it is
# a valid binary search tree (BST)*.
#
# A **valid BST** is defined as follows:
# *   The left subtree of a node contains only nodes with keys **less than** the node's key.
# *   The right subtree of a node contains only nodes with keys **greater than** the node's key.
# *   Both the left and right subtrees must also be binary search trees.
#
# Example 1:
# Input: root = [2,1,3]
# Output: true
#
# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.inorder(root, -float('inf'), float('inf'))

    def inorder(self, root, lower, upper):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        # 调用左子树时，因为左子树里所有节点的值均小于它的根节点的值，更改上界
        return self.inorder(root.left, lower, root.val) \
        # 调用右子树时，因为右子树里所有节点的值均大于它的根节点的值，更改下界
            and self.inorder(root.right, root.val, upper)