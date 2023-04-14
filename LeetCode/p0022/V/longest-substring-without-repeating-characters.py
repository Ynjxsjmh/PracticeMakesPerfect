# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: longest-substring-without-repeating-characters.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 17:07
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        l = 0
        lookup = {}
        cur_max_len = 0

        for r in range(len(s)):
            # If s[r] not in seen,
            # keep increasing the window size by moving right pointer (next loop)
            if s[r] not in lookup:
                cur_max_len = max(cur_max_len, r-l+1)
            else:
                if lookup[s[r]] < l:
                    # s[r] is not inside the current window,
                    # keep increase the window
                    cur_max_len = max(cur_max_len, r-l+1)
                else:
                    # s[r] is inside the current window,
                    # change the window by moving left pointer to seen[s[r]] + 1.
                    l = lookup[s[r]] + 1
            lookup[s[r]] = r

        return cur_max_len
