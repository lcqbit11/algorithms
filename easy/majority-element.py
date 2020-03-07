#!/usr/bin/env python
# -*- coding: utf-8 -*-


def majorityElement(nums):
    """
    给定一个数组，长度为n，其主要元素为在数组中出次数大于n/2次的数字，请找出来
    :param nums: List[int]
    :return major number: int
    """
    return sorted(nums)[int(len(nums)/2)]


def majorityElement1(nums):
    res = 0
    cnt = 0
    for i in range(0, len(nums)):
        if cnt == 0:
            cnt += 1
            res = nums[i]
        elif res != nums[i]:
            cnt -= 1
        else:
            cnt += 1

    return res


def majorityElement2(nums):
    def partition(nums, low, high):
        pivot = nums[high]
        index = low - 1
        for i in range(low, high):
            if nums[i] <= pivot:
                index += 1
                if index != i:
                    tmp = nums[index]
                    nums[index] = nums[i]
                    nums[i] = tmp
        index += 1
        tmp = nums[index]
        nums[index] = nums[high]
        nums[high] = tmp

        return index
    
    mid = int((len(nums) - 1) / 2)
    low, high = 0, len(nums)-1
    split_index = partition(nums, low, high)
    while split_index + 1 != mid:
        if split_index + 1 > mid:
            split_index = partition(nums, low, split_index - 1)
        else:
            split_index = partition(nums, split_index + 1, high)
       
    return split_index


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majorityElement2(nums))