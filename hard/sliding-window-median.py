#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize the data structure here.
        """
        self.maxHeap = []
        self.minHead = []

    def addNum(self, num):
        """
        :param num: int
        :return: None
        """
        heapq.heappush(self.maxHeap, -num)
        maxV = self.maxHeap[0] if self.maxHeap else None
        minV = self.minHead[0] if self.minHead else None
        if minV and minV < -maxV or (len(self.minHead) + 1) < len(self.maxHeap):
            heapq.heappush(self.minHead, -heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHead):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHead))

    def findMedian(self):
        """
        :return: float
        """
        if len(self.minHead) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHead[0] - self.maxHeap[0]) / 2.0

def sliding_window_median(nums, k):
    """
    给定一个整数数组和一个整数k，且k不大于数组的长度，一个长度k的滑动窗口从数组的最左侧划向最右侧，
    在每个滑动窗口所包含的数组元素中，找出中间值，并最终返回每个所有滑动窗口下的中间值。
    中间值定义：
        1.如果有偶数个元素，则返回按照大小排序后最中间两个的平均值;
        2.如果有奇数个元素，则返回按照大小排序后最中间一个值。
    :param nums: List[int]
    :return: List[float]
    """
    res = []
    for i in range(len(nums) - k + 1):
        mf = MedianFinder()
        for j in range(i, i + k):
            mf.addNum(nums[j])
        res.append(mf.findMedian())

    return res

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sliding_window_median(nums, k))