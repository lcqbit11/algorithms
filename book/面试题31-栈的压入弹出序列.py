#!/usr/bin/env python
# -*- coding: utf-8 -*-


def judge_pop_array(nums1, nums2):
    """
    输入两个整数序列，第一个序列表示栈的压入序列，请判断第二个序列是否为该栈的弹出序列
    :param nums1: List[int]
    :param nums2: List[int]
    :return: bool
    """
    nums = [nums1[0]]
    l1 = len(nums1)
    l2 = len(nums2)
    i = 0
    j = 0
    while i < l1:
        if not nums:
            return True
        while nums2[j] != nums[-1]:
            i += 1
            if i < l1:
                nums.append(nums1[i])
            else:
                return False
        nums.pop()
        j += 1
    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    # nums2 = [4, 5, 3, 2, 1]
    nums2 = [4, 3, 5, 1, 2]
    print(judge_pop_array(nums1, nums2))
