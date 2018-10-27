# -*- coding: utf-8 -*-
"""
16. 3Sum Closest

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


解题思路：
和15题解法差不多，只是这里只需要三个数的和，而且不用处理重复情况的逻辑，
就是多加一个变量，用于判断是否最接近target，这个变量初始值一定要大，以免
在判断时把一些满足条件的三元组过滤掉

"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        result = 0
        distance = pow(2, 32) - 1    # 初始化一个足够大的值
        length = len(nums)
        i = 0
        while i < length - 2:
            j = i + 1
            k = length - 1

            while j < k:
                total = sum([nums[i], nums[j], nums[k]])
                if total == target:
                    return target

                # 当前三元组的和与target 相减 < distance
                # 说明 三元组的和 更接近 distance，应该替换掉distance
                if abs(total - target) < distance:
                    result = total
                    distance = abs(total - target)  # 维护一个三元组与target之间的差的最小值
                # 当前三元组和大于 distance，需要右指针左移一位，
                elif total > distance:
                    k -= 1
                else:
                    j += 1
            i += 1
        return result

    def threeSumClosest_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 花费时间最短
        nums.sort()
        length = len(nums)
        res_list = []

        for i, num in enumerate(nums[0:length - 2]):
            l = i + 1
            r = length - 1
            if num + nums[l] + nums[l + 1] > target:
                res_list.append(num + nums[l] + nums[l + 1])
            elif num + nums[r] + nums[r - 1] < target:
                res_list.append(num + nums[r] + nums[r - 1])
            else:
                while l < r:
                    total = num + nums[l] + nums[r]
                    res_list.append(total)
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        return target
        # 关键在于这个地方，用空间换时间策略，把三元组的和放在
        # res_list 列表中，然后按照x-target 排序，第一位就是最靠近
        # target 值的三元组和
        res_list.sort(key=lambda x: abs(x - target))
        return res_list[0]


if __name__ == '__main__':
    so = Solution()
    nums = [-1, 2, 1, -4, 5, 2, 6, 232]
    target = 3
    print(so.threeSumClosest(nums, target))
    print(so.threeSumClosest_v2(nums, target))
