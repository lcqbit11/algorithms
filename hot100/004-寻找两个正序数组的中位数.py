#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

def findMedianSortedArrays(nums1, nums2):
    def findKElem(nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return findKElem(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        l1_start = min(k//2, len1)
        l2_start = k - l1_start
        if nums1[l1_start-1] < nums2[l2_start-1]:
            return findKElem(nums1[l1_start:], nums2, k - l1_start)
        elif nums1[l1_start-1] > nums2[l2_start-1]:
            return findKElem(nums1, nums2[l2_start:], k - l2_start)
        else:
            return nums1[l1_start - 1]

    lens = len(nums1) + len(nums2)
    if lens % 2 == 1:
        return findKElem(nums1, nums2, lens//2 + 1)
    else:
        return (findKElem(nums1, nums2, lens//2) + findKElem(nums1, nums2, lens//2 + 1)) / 2


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
