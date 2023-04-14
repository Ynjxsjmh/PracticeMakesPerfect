# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: reorder-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 15:20:00
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        slow = fast = head

        # 找中点，slow 最后指向中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 逆序中点后面节点
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        beg = head
        end = prev

        while beg and end:
            next1 = beg.next
            next2 = end.next

            beg.next = end
            end.next = next1

            beg = next1
            end = next2
