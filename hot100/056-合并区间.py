#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/merge-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def merge(intervals):
    if not intervals or len(intervals) <= 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
