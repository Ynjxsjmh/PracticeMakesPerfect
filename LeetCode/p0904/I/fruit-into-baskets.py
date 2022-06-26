# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: fruit-into-baskets.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-06-26 18:05:14
# Last Updated: 
#           By: Ynjxsjmh
# Description: You are visiting a farm that has a single row of fruit
# trees arranged from left to right. The trees are represented by an
# integer array `fruits` where `fruits[i]` is the **type** of fruit
# the `ith` tree produces.
#
# You want to collect as much fruit as possible. However, the owner has
# some strict rules that you must follow:
#
# * You only have **two** baskets, and each basket can only hold a
#     **single type** of fruit. There is no limit on the amount of fruit
#     each basket can hold.
# * Starting from any tree of your choice, you must pick **exactly one
#     fruit** from **every** tree (including the start tree) while
#     moving to the right. The picked fruits must fit in one of your
#     baskets.
# * Once you reach a tree with fruit that cannot fit in your baskets,
#     you must stop.
#
# Given the integer array `fruits`, return *the **maximum** number of
# fruits you can pick*.
#
# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
#
# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
# Constraints:
# *   `1 <= fruits.length <= 105`
# *   `0 <= fruits[i] < fruits.length`
# ********************************************************************************


class Solution(object):
    def totalFruit(self, fruits):
        """假设现在的 fruits 序列为 121n
        那么 n 有三种可能：
        1. n == 1，1 已经在 basket 里，1 和“最后见到的种类”相同
           既然已经在 basket 里，“当前 basket 装的水果数量”加 1
           “最后见到的种类数量”也加 1
        2. n == 2，2 已经在 basket 里，2 和“最后见到的种类”不同
           既然已经在 basket 里，“当前 basket 装的水果数量”加 1
           “最后见到的种类”更新成 2，“最后见到的种类数量”重置为 1，
        3. n == 3，3 不在 basket 里
           “当前 basket 装的水果数量”为上个 basket “最后见到的种类数量”加 1
           （这个 1 为当前 3 这个不在原 basket 的水果的数量）
           “最后见到的种类”更新成 3，“最后见到的种类数量”重置为 1，
        :type fruits: List[int]
        :rtype: int
        """

        old_fruit = -1
        new_fruit = -1

        cur_cnt = 0
        max_cnt = 0
        new_fruit_cnt = 0

        for fruit in fruits:
            if fruit == old_fruit:
                cur_cnt += 1
                new_fruit_cnt = 1
                old_fruit = new_fruit
                new_fruit = fruit
            elif fruit == new_fruit:
                cur_cnt += 1
                new_fruit_cnt += 1
            else:
                cur_cnt = new_fruit_cnt + 1
                new_fruit_cnt = 1
                old_fruit = new_fruit
                new_fruit = fruit

            max_cnt = max(cur_cnt, max_cnt)

        return max_cnt
