# -*- coding: utf-8 -*-
"""
18. 4Sum

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


解题思路
类似于3Sum 的解法，先确定第一个数i, 然后确定第二数j, 接着和3Sum的做法一样了
下面代码中有相关注释部分
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        if sum(nums[:4]) > target or sum(nums[-4:]) < target:
            return res

        for i in range(n - 3):
            # 两种极端情况，当最大三个加nums[i]都比target 小，则取nums下一个（排序过了，递增）
            # 如果当前nums[i+1]至nums[i+4] 四个数都比target - nums[i] 大，继续递增小标i,很像二分查找
            if sum(nums[-3:]) < target - nums[i] or sum(nums[i + 1: i + 4]) > target - nums[i]:
                continue

            # 去除重复情况
            if i and nums[i - 1] == nums[i]:
                continue

            # 和 3Sum 算法差不多了
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                prefix = nums[i] + nums[j]

                if sum(nums[-2:]) < target - prefix or sum(nums[j + 1: j + 3]) > target - prefix:
                    continue

                start, end = j + 1, n - 1

                while start < end:
                    s = nums[start] + nums[end]
                    if s > target - prefix:
                        end -= 1
                    elif s < target - prefix:
                        start += 1
                    else:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # 去除重复情况
                        while 0 < start < n - 2 and nums[start] == nums[start - 1]:
                            start += 1
                        while 1 < end < n + 1 and nums[end] == nums[end + 1]:
                            end -= 1
        return res

    def fourSum_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()

        res = []

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                p = j + 1
                q = n - 1

                while p != q:
                    total = nums[i] + nums[j] + nums[p] + nums[q]
                    if total > target:
                        q -= 1
                    elif total < target:
                        p += 1
                    else:
                        list_sum = [nums[i], nums[j], nums[p], nums[q]]
                        if list_sum not in res:
                            res.append(list_sum)
                        p += 1
        #                         p += 1
        #                         q -= 1
        #                         while p < q and nums[p] == nums[p-1]:
        #                             p += 1
        #                         while p < q and nums[q] == nums[q+1]:
        #                             q -= 1
        return res

    # 还有种递归解法


if __name__ == '__main__':
    so = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(so.fourSum(nums, target))
    print(so.fourSum_v2(nums, target))
