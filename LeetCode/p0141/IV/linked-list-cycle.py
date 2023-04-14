# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: linked-list-cycle.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 10:59:26
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
