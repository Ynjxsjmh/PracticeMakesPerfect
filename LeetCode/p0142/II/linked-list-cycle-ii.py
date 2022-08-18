# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: linked-list-cycle-ii.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-19 02:14:16
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a linked list, return *the node
# where the cycle begins. If there is no cycle, return* `null`.
#
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the `next`
# pointer. Internally, `pos` is used to denote the index of the node
# that tail's `next` pointer is connected to (**0-indexed**). It is
# `-1` if there is no cycle. **Note that** `pos` **is not passed as a
# parameter**.
#
# **Do not modify** the linked list.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail
# connects to the second node.
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail
# connects to the first node.
#
# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
# Constraints:
# *   The number of the nodes in the list is in the range `[0, 104]`.
# *   `-105 <= Node.val <= 105`
# *   `pos` is `-1` or a **valid index** in the linked-list.
#
# **Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?
# ********************************************************************************



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """slow 与 fast 相遇时，再额外使用一个指针ptr指向链表头部；
        将它和 slow 每次向后移动一个位置，它们最终会在入环点相遇
        :type head: ListNode
        :rtype: ListNode
        """


        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head

        return None
