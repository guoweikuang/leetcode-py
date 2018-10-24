# -*- coding: utf-8 -*-
"""
12. Integer to Roman

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。


解题思路：

根据题目要求，可以列出一个表：


----------------------------
   阿拉伯数字   |    罗马数字
----------------------------
      1000    |       M
      900     |       CM
      500     |       D
      400     |       CD
      100     |       C
      90      |       XC
      50      |       L
      40      |       XL
      10      |       X
      9       |       IX
      5       |       V
      4       |       IV
      1       |       I
----------------------------
根据上面表对应关系，找出表中包含数字中可转化的最大罗马数字的数字即可，比如99，100比99大，而90刚好比99小，
是最大可转化的数字，减去还留下9， 对应表可直接转化成 XCIX
"""
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""

        nums_and_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""

        for n, roman in nums_and_roman:
            while num >= n:
                num -= n
                result += roman
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.intToRoman(3))
    print(so.intToRoman(4))
    print(so.intToRoman(9))
    print(so.intToRoman(58))
    print(so.intToRoman(1994))


