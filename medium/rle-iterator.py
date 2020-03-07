#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RLEIterator(object):
    """
    题目参考：https://leetcode.com/problems/rle-iterator/
    run-length encoding 行程编码。迭代器初始化为RLEIterator(int[] A)，其中A表示序列的行程编码，需要注意的是，
    对于任何偶数位的A[i]值，其表示了非负值A[i+1]重复出现的次数。其中元素位置从0开始算起，即 0，1，2，，，因此第一位为偶数位
    请编写一个遍历行程编码序列的迭代器，该迭代器支持函数next(int n)，意思是遍历之后的n个元素并返回该次遍历路径的最后一个元素，
    如果剩下的元素不够用来遍历的，那么返回 -1 ，举个例子：
    迭代器A=[3,8,0,9,2,5]，其表示序列[8,8,8,5,5]的行程编码，
    如果连续4次调用next函数，且入参分别为[[2],[1],[1],[2]]时，那么对应的next函数的返回结果为[8,8,5,-1]
    """
    def __init__(self, seq):
        self.seq = seq[::]

    def next(self, n):
        while n > 0 and len(self.seq) > 0:
            if self.seq[0] >= n:
                self.seq[0] -= n
                return self.seq[1]
            else:
                n -= self.seq[0]
                del self.seq[0]
                del self.seq[0]
                return self.next(n)
        return -1


if __name__ == "__main__":
    nums = [3,8,0,9,2,5]
    rle_iterator = RLEIterator(nums)
    print(rle_iterator.next(2))
    print(rle_iterator.next(1))
    print(rle_iterator.next(1))
    print(rle_iterator.next(2))