#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fast_sort(numbers, low, high):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    # 算法1
    def partition(nums_list, l, h):
        pivot = nums_list[h]
        k = l - 1
        for i in range(l, h):
            if nums_list[i] < pivot:
                k += 1
                nums_list[i], nums_list[k] = nums_list[k], nums_list[i]
        nums_list[k + 1], nums_list[h] = nums_list[h], nums_list[k + 1]
        return k + 1
    if low >= high:
        return
    split_index = partition(numbers, low, high)
    fast_sort(numbers, low, split_index - 1)
    fast_sort(numbers, split_index + 1, high)

    # 算法2
    # if low >= high:
    #     return
    # pivot = numbers[low]
    # start, end = low, high
    # while start < end:
    #     while start < end and numbers[end] >= pivot:
    #         end -= 1
    #     numbers[start] = numbers[end]
    #     while start < end and numbers[start] <= pivot:
    #         start += 1
    #     numbers[end] = numbers[start]
    # numbers[start] = pivot
    #
    # fast_sort(numbers, low, start - 1)
    # fast_sort(numbers, start + 1, high)

    # 算法3
    # if low >= high:
    #     return
    # pivot = numbers[low]
    # start, end = low, high
    # while start < end:
    #     while start < end and numbers[end] >= pivot:
    #         end -= 1
    #     while start < end and numbers[start] <= pivot:
    #         start += 1
    #     if start < end:
    #         numbers[start], numbers[end] = numbers[end], numbers[start]
    # numbers[low] = numbers[start]
    # numbers[start] = pivot

    # fast_sort(numbers, low, start-1)
    # fast_sort(numbers, start + 1, high)


if __name__ == "__main__":
    nums = [9, 3, 6, 2, 7, 1, 2]
    old = ""
    for number in nums:
        old += " "
        old += str(number)
    print(old)
    fast_sort(nums, 0, len(nums)-1)
    new = ""
    for number in nums:
        new += " "
        new += str(number)
    print(new)