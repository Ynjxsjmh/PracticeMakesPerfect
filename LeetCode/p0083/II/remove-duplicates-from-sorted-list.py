# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: remove-duplicates-from-sorted-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-23 15:04:15
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a sorted linked list, *delete all
# duplicates such that each element appears only once*. Return *the
# linked list **sorted** as well*.
#
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
# Constraints:
# *   The number of nodes in the list is in the range `[0, 300]`.
# *   `-100 <= Node.val <= 100`
# *   The list is guaranteed to be **sorted** in ascending order.
# ********************************************************************************



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0, head)

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next