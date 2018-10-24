# -*- coding: utf-8 -*-
"""
13. Roman to Integer

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。


解题思路：

根据规则，左边字母比右边小的情况下需要用 右边字母对应数字 减去 左边字母对应数字，
其它情况都是 相加的。这里对罗马字符进行循环，每取出一个和前一个进行对比数字大小，
需要注意的是，当前一个字母比后一个字母小的时候，需要先减去前一个字母的值，因为在
前一轮中已经加在最后结果里，减去前一个字母的值后，最后结果 += 后一个字母的数字 - 前一个字母数字

"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        nums_to_roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                         'X': 10, 'V': 5, 'I': 1}

        length = len(s)
        result = 0

        for i in range(length):
            if i and nums_to_roman[s[i]] > nums_to_roman[s[i - 1]]:
                result -= nums_to_roman[s[i - 1]]
                result += nums_to_roman[s[i]] - nums_to_roman[s[i - 1]]
            else:
                result += nums_to_roman[s[i]]
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.romanToInt('III'))
    print(so.romanToInt("IV"))
    print(so.romanToInt("IX"))
    print(so.romanToInt("LVIII"))
    print(so.romanToInt('MCMXCIV'))