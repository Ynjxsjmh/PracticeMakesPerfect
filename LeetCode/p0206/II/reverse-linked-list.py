# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: reverse-linked-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-23 10:34:02
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a singly linked list, reverse the
# list, and return *the reversed list*.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
# *   The number of nodes in the list is the range `[0, 5000]`.
# *   `-5000 <= Node.val <= 5000`
#
# **Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?
# ********************************************************************************



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        rhead = None

        while head:
            next_ = head.next
            head.next = rhead
            rhead = head
            head = next_

        return rhead
