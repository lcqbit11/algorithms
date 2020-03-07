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

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    mf.addNum(4)
    print(mf.findMedian())