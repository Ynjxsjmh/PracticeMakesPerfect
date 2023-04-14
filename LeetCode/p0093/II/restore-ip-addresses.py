# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2023 Ynjxsjmh
# File Name: restore-ip-addresses.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2023-04-14 20:44:05
# Last Updated: 
#           By: Ynjxsjmh
# Description: 
# ********************************************************************************


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, 0, '', res)
        return res

    def dfs(self, s, beg, part, mid_res, res):
        # 每个 ip 地址由四部分组成
        if part == 4:
            # 已经有 part 0, 1, 2, 3 四部分了
            if beg == len(s):
                res.append(mid_res[:-1])
            return

        # 每部分最多 3 个字符
        for end in range(beg, beg+4):
            ip = s[beg:end+1]

            # 判断当前 ip 合不合法，以下两种情况不合法
            # 1. ip 长度大于 1，且第一个字符为 0
            # 2. ip 大于 255
            if not ((len(ip) > 1 and ip[0] == '0') or (len(ip) and int(ip) > 255)):
                # 进行下一部分的判断
                self.dfs(s, end+1, part+1, mid_res+ip+".", res)
