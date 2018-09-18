# -*- coding: utf-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

判断是否回文，可以依次获取数字的首尾数字进行比较。数字首位可从循环获取，尾部通过% 获取。
"""

class Solution:
    def is_palindrome(self, x):
        if x < 0:
            return False

        div = 1
        # 循环获取div为了下面步骤得到首位数字
        while x / div >= 10:
            div *= 10

        while x > 0:
            l = x // div  # 首位
            r = x % 10   # % 获取尾部

            if l != r:
                return False

            x %= div  # 除去首位
            x //= 10  # 除去尾位
            div //= 100  # 最高位除数相应除去100

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.is_palindrome(12321))
    print(solution.is_palindrome(123))

