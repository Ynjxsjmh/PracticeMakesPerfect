# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: merge-two-sorted-lists.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-22 01:43:12
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given the heads of two sorted linked lists
# `list1` and `list2`.
#
# Merge the two lists in a one **sorted** list. The list should be
# made by splicing together the nodes of the first two lists.
#
# Return *the head of the merged linked list*.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# *   The number of nodes in both lists is in the range `[0, 50]`.
# *   `-100 <= Node.val <= 100`
# *   Both `list1` and `list2` are sorted in **non-decreasing** order.
# ********************************************************************************



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        head = dummy

        while list1 or list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')

            if val1 < val2:
                val = val1
                list1 = list1.next
            else:
                val = val2
                list2 = list2.next

            head.next = ListNode(val)
            head = head.next

        return dummy.next
