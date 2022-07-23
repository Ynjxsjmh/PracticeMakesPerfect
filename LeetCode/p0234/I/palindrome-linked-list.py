# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: palindrome-linked-list.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-23 14:50:27
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given the `head` of a singly linked list, return `true`
# if it is a palindrome.
#
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
# Input: head = [1,2]
# Output: false
#
# Constraints:
# *   The number of nodes in the list is in the range `[1, 105]`.
# *   `0 <= Node.val <= 9`
#
# **Follow up:** Could you do it in `O(n)` time and `O(1)` space?
# ********************************************************************************


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        s = ''

        while head:
            s += str(head.val)
            head = head.next

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
