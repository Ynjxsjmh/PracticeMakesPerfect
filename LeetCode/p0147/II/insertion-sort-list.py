# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: insertion-sort-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-29 15:44:28
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a singly linked list, sort the list
# using **insertion sort**, and return *the sorted list's head*.
#
# The steps of the **insertion sort** algorithm:
#
# 1.  Insertion sort iterates, consuming one input element each
# repetition and growing a sorted output list.
#
# 2.  At each iteration, insertion sort removes one element from the
# input data, finds the location it belongs within the sorted list and
# inserts it there.
# 3.  It repeats until no input elements remain.
#
# The following is a graphical example of the insertion sort
# algorithm. The partially sorted list (black) initially contains only
# the first element in the list. One element (red) is removed from the
# input data and inserted in-place into the sorted list with each
# iteration.
#
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
# Constraints:
# *   The number of nodes in the list is in the range `[1, 5000]`.
# *   `-5000 <= Node.val <= 5000`
# ********************************************************************************



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        dummy.next = head

        last_sort = head
        cur = head.next

        while cur:
            if last_sort.val <= cur.val:
                last_sort = last_sort.next
            else:
                slow = dummy
                fast = dummy.next

                while fast.val <= cur.val:
                    slow = slow.next
                    fast = fast.next

                last_sort.next = cur.next
                slow.next = cur
                cur.next = fast

            cur = last_sort.next

        return dummy.next
