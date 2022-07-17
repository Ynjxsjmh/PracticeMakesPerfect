# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: odd-even-linked-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-18 02:49:44
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a singly linked list, group all the
# nodes with odd indices together followed by the nodes with even
# indices, and return *the reordered list*.
#
# The **first** node is considered **odd**, and the **second** node is
# **even**, and so on.
#
# Note that the relative order inside both the even and odd groups
# should remain as it was in the input.
#
# You must solve the problem in `O(1)` extra space complexity and
# `O(n)` time complexity.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
# Constraints:
# *   The number of nodes in the linked list is in the range `[0, 104]`.
# *   `-106 <= Node.val <= 106`
# ********************************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        # 1 ---> 2 ---> 3 ---> 4 --->
        # o      e
        even_head = head.next
        odd, even = head, even_head

        while even and even.next:
            # 把偶节点从奇链拿下来
            # 1 ----------> 3 ---> 4 --->
            #        2
            # o      e
            odd.next = even.next
            # 1 ----------> 3 ---> 4 --->
            #        2
            #        e      o
            odd = odd.next
            # 1 ----------> 3 ---> 4 --->
            #        2 ---------->
            #        e      o
            even.next = odd.next
            # 1 ----------> 3 ---> 4 --->
            #        2 ---------->
            #               o      e
            even = even.next

        odd.next = even_head

        return head
