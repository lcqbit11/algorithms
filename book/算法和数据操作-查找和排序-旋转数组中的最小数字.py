#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rotate_array_min_number(numbers):
    """
    :param numbers: List[int]
    :return: int
    """
    start, end = 0, len(numbers)-1
    while end - start > 1:
        middle = int((start + end) / 2)
        if numbers[middle] >= numbers[start]:
            start = middle
        elif numbers[middle] <= numbers[end]:
            end = middle
    if end-start == 1:
        return numbers[end]
    return

if __name__ == "__main__":
    numbers = [3, 4, 5, 6, 7, 1, 2]
    print(rotate_array_min_number(numbers))