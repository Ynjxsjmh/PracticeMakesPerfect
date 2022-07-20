# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2022 Ynjxsjmh
# File Name: implement-trie-prefix-tree.py
# Author: Ynjxsjmh
# Email: ynjxsjmh@gmail.com
# Created: 2022-07-20 13:14:04
# Last Updated: 
#           By: Ynjxsjmh
# Description: A [**trie**](https://en.wikipedia.org/wiki/Trie)
# (pronounced as "try") or **prefix tree** is a tree data structure
# used to efficiently store and retrieve keys in a dataset of
# strings. There are various applications of this data structure, such
# as autocomplete and spellchecker.
#
# Implement the Trie class:
# *   `Trie()` Initializes the trie object.
# *   `void insert(String word)` Inserts the string `word` into the trie.
# *   `boolean search(String word)` Returns `true` if the string
#     `word` is in the trie (i.e., was inserted before), and `false`
#     otherwise.
# *   `boolean startsWith(String prefix)` Returns `true` if there is a
#     previously inserted string `word` that has the prefix `prefix`,
#     and `false` otherwise.
#
# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
# Constraints:
# *   `1 <= word.length, prefix.length <= 2000`
# *   `word` and `prefix` consist only of lowercase English letters.
# *   At most `3 * 104` calls **in total** will be made to `insert`, `search`, and `startsWith`.
# ********************************************************************************



class Trie(object):

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]

        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)