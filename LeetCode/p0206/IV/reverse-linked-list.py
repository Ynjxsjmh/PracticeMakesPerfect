# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: reverse-linked-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 09:30:06
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev
