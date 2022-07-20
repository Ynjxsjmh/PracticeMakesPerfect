# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: merge-k-sorted-lists.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-20 14:25:26
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are given an array of `k` linked-lists `lists`,
# each linked-list is sorted in ascending order.
#
# *Merge all the linked-lists into one sorted linked-list and return
# *it.*
#
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
# Input: lists = []
# Output: []
#
# Example 3:
# Input: lists = [[]]
# Output: []
#
# Constraints:
# *   `k == lists.length`
# *   `0 <= k <= 104`
# *   `0 <= lists[i].length <= 500`
# *   `-104 <= lists[i][j] <= 104`
# *   `lists[i]` is sorted in **ascending order**.
# *   The sum of `lists[i].length` will not exceed `104`.
# ********************************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Time Limit Exceeded  132 / 133 test cases passed.
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummy = ListNode()
        head = dummy

        while self.not_end(lists):
            vals = [node.val if node else float('inf') for node in lists]
            min_val = min(vals)

            for i, node in enumerate(lists):
                if node and node.val == min_val:
                    lists[i] = node.next
                    break

            cur = ListNode(min_val)
            head.next = cur
            head = head.next

        return dummy.next

    def not_end(self, lists):
        not_end = False

        for node in lists:
            not_end = not_end or node

        return not_end

    def mergeTwoLists(self, listNode1, listNode2):
        dummy = ListNode()
        head = dummy

        while listNode1 and listNode2:
            if listNode1.val < listNode2.val:
                head.next = ListNode(listNode1.val)
                listNode1 = listNode1.next
            else:
                head.next = ListNode(listNode2.val)
                listNode2 = listNode2.next
            head = head.next

        head.next = listNode1 or listNode2
        return dummy.next

    def merge(self, lists, l, r):
        if (l == r): return lists[l]
        if (l > r): return None
        mid = (l + r) >> 1
        return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def mergeKLists(self, lists):
        return self.merge(lists, 0, len(lists)-1)
