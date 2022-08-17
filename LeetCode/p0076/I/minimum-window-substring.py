# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: minimum-window-substring.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-02 15:54:57
# Last Updated: 
#           By: Ynjxsjmh
# Description: Given two strings `s` and `t` of lengths `m` and `n`
# respectively, return *the **minimum window substring** of* `s` *such
# that every character in* `t` *(**including duplicates**) is included
# in the window. If there is no such substring**, return the empty
# string* `""`*.*
#
# The testcases will be generated such that the answer is **unique**.
#
# A **substring** is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
# Constraints:
# *   `m == s.length`
# *   `n == t.length`
# *   `1 <= m, n <= 105`
# *   `s` and `t` consist of uppercase and lowercase English letters.
#
# **Follow up:** Could you find an algorithm that runs in `O(m + n)` time?
# ********************************************************************************



class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 维护两个数组，记录目标字符串字符频数和窗口字符串字符字符频数
        # ASCII表总长128
        need, have = [0]*128, [0]*128

        for ch in t:
            need[ord(ch)] += 1

        # 窗口左指针，窗口右指针，最小覆盖子串在原字符串中的起始位置
        l, r, start = 0, 0, 0
        # 最小长度, 窗口字符串中“目标字符串中字符的出现总频次”
        # count 的理解是关键，但是语言功底不够很难言传出来。
        # 比如目标字符串是 ABB，窗口字符串是 ABBBC
        # 目标字符串中 B 出现了两次，窗口字符串中 B 出现了三次，但count只记录目标字符串的两次
        # 这样如果 count 如果等于目标字符串的长度，说明窗口字符串包含了目标字符串的所有字符
        min_len, count = float('inf'), 0

        while r < len(s):
            s_r = ord(s[r])
            # 如果窗口右边字符不被目标字符串需要，此时有两种情况
            # 1. 刚开始循环，那么直接移动右指针即可，不需要做多余判断
            # 2. 循环已经开始一段时间，此处又有两种情况
            #   2.1 上一次条件不满足，窗口字符串各个字符出现次数不满足目标字符串各个字符出现次数，
            #       那么此时如果该字符还不被目标字符串需要，就不需要进行多余判断，右指针移动即可
            #   2.2 左指针已经移动完毕，那么此时就相当于循环刚开始，同理直接移动右指针
            if need[s_r] == 0:
                r += 1
                continue

            # 当且仅当窗口字符串目标字符出现的次数小于目标字符串字符的出现次数时，count才会+1
            # 方便后续能直接判断窗口字符串是否已经包含了目标字符串的所有字符
            if have[s_r] < need[s_r]:
                count += 1

            # 窗口字符串中目标字符出现的次数+1
            have[s_r] += 1

            # 移动右指针
            r += 1

            # 当且仅当窗口字符串已经包含了所有目标字符串的字符，
            # 且出现频次一定大于或等于指定频次
            while count == len(t):
                # 当窗口的长度比已有的最短值小时，
                # 更改最小值，并记录起始位置
                if r - l < min_len:
                    min_len = r - l
                    start = l

                s_l = ord(s[l])
                # 如果左边即将要去掉的字符不是目标字符串需要的，
                # 那么不需要多余判断，可以直接移动左指针
                if need[s_l] == 0:
                    l += 1
                    continue

                # 如果左边即将要去掉的字符是目标字符串需要的，且出现的频次正好等于指定频次，
                # 那么如果去掉了这个字符，那么窗口字符串内该字符就比目标字符串该字符少了，
                # 即不满足覆盖子串的条件，将“目标字符串中字符的出现总频次”(count）-1后，
                # 会破坏循环条件跳出循环
                if have[s_l] == need[s_l]:
                    count -= 1

                # 窗口字符串中目标字符出现的次数-1
                have[s_l] -= 1
                # 移动左指针
                l += 1

        return '' if min_len == float('inf') else s[start:start+min_len]


    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        dict_t, counter = Counter(t), len(t)

        # left and right pointer
        l, r, head = 0, 0, 0

        min_len = float('inf')

        while r < len(s):
            # 1. If character at r is present in T then
            # 2. If count of that character in hashmap
            #    is greater than zero then decrement the counter
            # 3. Decrement the count for that character in hashmap
            if s[r] in dict_t:
                if dict_t[s[r]] > 0:
                    counter -= 1
                dict_t[s[r]] -= 1

            r += 1

            # While counter is zero,
            # it means we have all characters of t between l and r.
	    # That's to say we found a valid window,
            # we then need move start to find smaller window.
            while counter == 0:
                # Update min_len here if finding minimum
                if r - l < min_len:
                    min_len = r - l
                    head = l

                # If character at l is present in T,
                # then increment its count in hashmap
                #
                #   If its count in hashmap is <= 0,
                #   then continue the inner while loop until the count is positive
                #
                #   If its count in hashmap is > 0,
                #   then increment the counter and continue searching .
                if s[l] in dict_t:
                    dict_t[s[l]] += 1
                    if dict_t[s[l]] > 0:
                        counter += 1

                l += 1

        return '' if min_len == float('inf') else s[head:head+min_len]
