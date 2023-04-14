# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: merge-two-sorted-lists.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 11:08:29
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next
