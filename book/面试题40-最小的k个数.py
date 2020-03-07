#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from lib.treeNode import TreeNode


class Solution(object):
    # 时间复杂度为O(n)的算法
    def min_k_num(self, nums, k):
        """
        给定一个无序数组，输出其中最小的k个数值。
        借鉴快速排序中的partition操作，直到当前的pivot的位置为数组的第k个位置即可。时间复杂度为O(n)。
        """
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot

            return left

        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        index = partition(nums, start, end)
        while index != k - 1:
            if index > k - 1:
                index = partition(nums, start, index - 1)
            else:
                index = partition(nums, index + 1, end)
        
        return nums[:index+1]

    def min_k_num1(self, nums, k):
        """
        给定一个无序数组，输出其中最小的k个数值。
        此处可以使用大顶堆来做，时间复杂度为O(nlogk)。
        """
        def max_heap(nums, start, end):
            index = start
            k = 2 * index + 1
            while k <= end:
                if k + 1 <= end and nums[k] < nums[k + 1]:
                    k += 1
                if nums[index] < nums[k]:
                    nums[index], nums[k] = nums[k], nums[index]
                    index = k
                    k = 2 * index + 1
                else:
                    break
                
        if not nums:
            return 
        mid = int((k - 1) / 2)
        for i in reversed(range(0, mid+1)):
            max_heap(nums, i, k - 1)
        
        l = len(nums)
        for i in range(k, l):
            if nums[0] > nums[i]:
                nums[0], nums[i] = nums[i], nums[0]
                max_heap(nums, 0, k - 1)
        
        return nums[:k]

            
if __name__ == "__main__":
    nums = [4, 5, 1, 6, 2, 9, 7, 3, 8]
    solu = Solution()
    print(solu.min_k_num(nums, 3))