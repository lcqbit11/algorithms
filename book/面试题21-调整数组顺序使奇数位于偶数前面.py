#!/usr/bin/env python
# -*- coding: utf-8 -*-

def odd_head_of_even(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    def is_even(n):
        return (n & 1) == 0

    start, end = 0, len(numbers)-1
    while start < end:
        while start < end and not is_even(numbers[start]):
            start += 1
        while start < end and is_even(numbers[end]):
            end -= 1
        if start < end:
            numbers[start] = numbers[start]+numbers[end]
            numbers[end] = numbers[start]-numbers[end]
            numbers[start] = numbers[start]-numbers[end]
    return numbers

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(odd_head_of_even(numbers))