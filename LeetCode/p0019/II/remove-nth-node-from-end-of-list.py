# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: remove-nth-node-from-end-of-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-22 15:54:21
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a linked list, remove the `nth`
# node from the end of the list and return its head.
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# *   The number of nodes in the list is `sz`.
# *   `1 <= sz <= 30`
# *   `0 <= Node.val <= 100`
# *   `1 <= n <= sz`
#
# **Follow up:** Could you do this in one pass?
# ********************************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """双指针，一个先到 n 的位置
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        first = head
        dummy = ListNode(0, head)
        second = dummy

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
