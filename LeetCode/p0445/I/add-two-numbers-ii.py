# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: add-two-numbers-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-14 16:12:11
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given two **non-empty** linked lists
# representing two non-negative integers. The most significant digit
# comes first and each of their nodes contains a single digit. Add the
# two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
#
# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
#
# Example 3:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Constraints:
# *   The number of nodes in each linked list is in the range `[1, 100]`.
# *   `0 <= Node.val <= 9`
# *   It is guaranteed that the list represents a number that does not have leading zeros.
# ********************************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            val = val1 + val2 + carry

            carry = val // 10
            curNode = ListNode(val % 10)
            curNode.next = head
            head = curNode

        return head
