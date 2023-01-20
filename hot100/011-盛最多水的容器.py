#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def maxArea(height):
    if len(height) < 2:
        return 0

    left, right = 0, len(height) - 1
    res = 0
    while left < right:
        res = max(res, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
