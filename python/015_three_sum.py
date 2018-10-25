# -*- coding: utf-8 -*-
"""
15. 3Sum

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


解题思路：
求二元组之间和为零的列表的思路就是将列表先进行排序，再用头尾指针向中间迭代，
当二元组和 > 0时，右边指针-1即是右移， 当二元组和 < 0时，左边指针 + 1即是左移。
这里是求三元组求和，也可使用类似方法， 先确定第一个数字a，然后就相当于求一个二元组
等于-a 的值，这里需要注意的是，遇到重复的组合需要直接过滤掉。


"""
from itertools import combinations


class Solution:
    def threeSum(self, nums):
        """
        不通过
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = combinations(nums, 3)
        res = []
        temp = []
        for i, j, z in nums:
            if i + j + z == 0:
                s = list(sorted([i, j, z]))
                int_to_str = "".join(map(str, s))
                if int_to_str not in temp:
                    temp.append(int_to_str)
                    res.append(s)

        return res

    def threeSum_v1(self, nums):
        result = []
        nums.sort()
        i = 0

        length = len(nums)

        while i < length - 2:
            if i and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = length - 1

            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) > 0:
                    k -= 1

                elif sum(l) < 0:
                    j += 1
                else:
                    result.append(l)

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.threeSum([-1, 0, 1, 2, -1, -4]))
    print(so.threeSum_v1([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))