#!/usr/bin/env python
# -*- coding: utf-8 -*-

def median_of_two_sorted_arrays(numbers1, numbers2):
    """
    有两个排序后的数组，长度分别为m，n，请找出他们的中位数，并且控制时间复杂度在O(log(m+n))
    :param numbers1: List[int]
    :param numbers2: List[int]
    :return: double
    """
    def find_median(nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return find_median(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        l1_start = min(int(k/2), len1)
        l2_start = k - l1_start
        if nums1[l1_start - 1] < nums2[l2_start - 1]:
            # 此时，nums1[l1_start - 1]最好情况下为第k-1大的数字，
            # 所以第k位数字不可能在出现nums1的 (l1_start - 1) 及之前
            return find_median(nums1[l1_start:], nums2,  k - l1_start)
        elif nums1[l1_start - 1] > nums2[l2_start - 1]:
            return find_median(nums1, nums2[l2_start:], k - l2_start)
        else:
            return nums2[l2_start - 1]

    l1 = len(numbers1)
    l2 = len(numbers2)
    len_sum = l1 + l2
    if len_sum % 2 == 1:
        return find_median(numbers1, numbers2, int(len_sum / 2) + 1)
    else:
        return (find_median(numbers1, numbers2, int(len_sum / 2)) + find_median(numbers1, numbers2, int(len_sum / 2) + 1)) / 2

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(median_of_two_sorted_arrays(nums1, nums2))