# -*- coding: utf-8 -*-
"""
14. Longest Common Prefix

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。


解题思路：
选择一个字符最短的作为参考，然后迭代strs 列表中的所有字符是否和最短字符里的字符一一对应，如不对应
跳出循环，返回当前0-当前下标的字符

"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        short_str = min(strs, key=len)

        for i, s in enumerate(short_str):
            for str in strs:
                if str[i] != s:
                    return short_str[:i]
        return short_str

    def longestCommonPrefix_v1(self, strs):
        if not strs:
            return ''

        a = min(strs)
        b = max(strs)
        for i in range(len(a)):
            if a[i] != b[i]:
                return a[0:i]
        return a

    def longestCommonPrefix_v2(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for str in strs:
                if str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix_v3(self, strs):
        if not strs:
            return ""

        short_str = min(strs)
        long_str = max(strs)

        for i, s in enumerate(short_str):
            if long_str[i] != s:
                return short_str[:i]
        return short_str


if __name__ == '__main__':
    so = Solution()
    print(so.longestCommonPrefix(["flower", "flow", "flight"]))
    print(so.longestCommonPrefix_v1(["flower", "flow", "flight"]))
    print(so.longestCommonPrefix_v2(["flower", "flow", "flight"]))
    print(so.longestCommonPrefix_v3(["flower", "flow", "flight"]))