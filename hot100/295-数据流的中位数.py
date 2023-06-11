#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:

# MedianFinder() 初始化 MedianFinder 对象。

# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-median-from-data-stream
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []


    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)
        maxValue = self.maxHeap[0] if self.maxHeap else None
        minvalue = self.minHeap[0] if self.minHeap else None
        if (minvalue and minvalue < -maxValue) or (len(self.minHeap)+1 < len(self.maxHeap)):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self):
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0]-self.maxHeap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
