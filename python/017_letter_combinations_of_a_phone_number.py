# -*- coding: utf-8 -*-
"""
17. Letter Combinations of a Phone Number

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

解题思路：
首先我们已经知道数字与字母的对应关系，可以总结在一个字典中，
然后使用深度遍历方式获取所有路径（形式上）和判断树从根节点到
叶子节点有多少条路径一样
如 "23":
            root
        /     |     \
       a      b      c
     / | \  / | \  / | \
     d e f  d e f  d e  f
"""

from itertools import combinations


class Solution:
    num_to_letter = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = []
        # 深度遍历
        self.dfs(digits, '', result)
        return result

    def dfs(self, digits, current, result):
        if not digits:
            result.append(current)
            return

        for c in self.num_to_letter[digits[0]]:
            self.dfs(digits[1:], current + c, result)  # 记得每次递归一个digits，都有把current加进去

    def letterCombinations_v2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combs = [""]
        for digit in digits:
            new_combs = []
            for comb in combs:
                for letter in mapping[digit]:
                    new_combs.append(comb + letter)
            combs = new_combs

        return combs


if __name__ == '__main__':
    so = Solution()
    print(so.letterCombinations("23"))
    print(so.letterCombinations_v2("23"))