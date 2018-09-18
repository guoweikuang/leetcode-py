# -*- coding: utf-8 -*-
"""
11. 盛最多水的容器

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


解题思路：

这个就是木桶原理的题目，装水的容量取决于最短那个板，而我们要做的是找到一个板使得容纳水最多，
可以通过左板(left)、右板(right)的移动来判断容水量，如果左板短，计算当前左右板之间的容水量，与最大容水量(result)
比较，大的话就更新最大容水量，并更新左板+1(换个左板看看能不能更大容水），反之也是这样, 但要保证一个前提，
左板的移动不能超过右板的位置(left < right)
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        # 一个以下的板直接返回0
        if length < 1:
            return 0

        # 左右板的下标
        left = 0
        right = length - 1

        # 最大容水量
        result = 0

        # 保证左板不超过右板
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left) # 计算两板之间容量，高度取最短板
                result = max(area, result)   # 更新最大容量值
                left += 1 # 换下一个左板
            else:
                area = height[right] * (right - left)
                result = max(area, result)
                right -= 1 # 换下一个右板
        return result


if __name__ == '__main__':
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))

