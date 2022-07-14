# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: add-two-numbers.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-14 15:47:22
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given two **non-empty** linked lists
# representing two non-negative integers. The digits are stored in
# **reverse order**, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
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

        dummy = ListNode()
        pre = 0
        head = dummy
        while l1 or l2 or pre:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + pre
            pre = val // 10

            head.next = ListNode(val % 10)
            head = head.next

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

        return dummy.next
