#!/usr/bin/env python
# -*- coding: utf-8 -*-


def longest_consecutive(nums):
    """
    给定一个无序的数组，请输出数组中连续值元素序列的最长长度。需要给出时间复杂度为O(n)的解法。
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    d = {x: False for x in nums}
    max_len = -1
    for i in d:
        if not d[i]:
            curr = i + 1
            len_right = 0
            while curr in d:
                len_right += 1
                d[curr] = True
                curr += 1

            curr = i - 1
            len_left = 0
            while curr in d:
                len_left += 1
                d[curr] = True
                curr -= 1

            max_len = max(max_len, len_left + 1 + len_right)
    return max_len


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))