# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: lru-cache.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-08-05 02:48:07
# Last Updated: 
#           By: Ynjxsjmh
# Description: Design a data structure that follows the constraints of
# a **[Least Recently Used (LRU)
# cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.
#
# Implement the `LRUCache` class:
#
# * `LRUCache(int capacity)` Initialize the LRU cache with **positive**
#     size `capacity`.
# * `int get(int key)` Return the value of the `key` if the key exists,
#     otherwise return `-1`.
# * `void put(int key, int value)` Update the value of the `key` if the
#     `key` exists. Otherwise, add the `key-value` pair to the cache. If
#     the number of keys exceeds the `capacity` from this operation,
#     **evict** the least recently used key.
#
# The functions `get` and `put` must each run in `O(1)` average time complexity.
#
# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# * LRUCache lRUCache = new LRUCache(2);
# * lRUCache.put(1, 1); // cache is {1=1}
# * lRUCache.put(2, 2); // cache is {1=1, 2=2}
# * lRUCache.get(1);    // return 1
# * lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# * lRUCache.get(2);    // returns -1 (not found)
# * lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# * lRUCache.get(1);    // return -1 (not found)
# * lRUCache.get(3);    // return 3
# * lRUCache.get(4);    // return 4
#
# Constraints:
# *   `1 <= capacity <= 3000`
# *   `0 <= key <= 104`
# *   `0 <= value <= 105`
# *   At most 2` * 105` calls will be made to `get` and `put`.
# ********************************************************************************


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.max_size = capacity
        # key -> DLinkedNode
        self.cache = {}

    def get(self, key):
        """
        1. key 不存在，返回 -1
        2. key 存在，先通过哈希表定位，返回 value 值并将该节点移到双向链表的头部
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        1. 如果 key 不存在，添加 key，并将 key 和该节点添加进哈希表中
           1.1 判断双向链表的节点数是否超出容量，
               如果超出容量，则删除双向链表的尾部节点，并删除哈希表中对应的项；
        2. 如果 key 存在，先通过哈希表定位，再将对应的节点的值更新为 value，
           并将该节点移到双向链表的头部。
        :type key: int
        :type value: int
        :rtype: None
        """

        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)

            self.size += 1
            if self.size > self.max_size:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)