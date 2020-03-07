#!/usr/bin/env python
# -*- coding: utf-8 -*-

def helan_flag(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    left, right = 0, len(numbers)-1
    i = 0
    while i <= right:
        if numbers[i] < 1:
            numbers[left], numbers[i] = numbers[i], numbers[left]
            left += 1
            i += 1
        elif numbers[i] > 1:
            numbers[right], numbers[i] = numbers[i], numbers[right]
            right -= 1
        else:
            i += 1

    return numbers

if __name__ == "__main__":
    numbers = [2, 1, 2, 0, 0, 2, 1, 0]
    print(numbers)
    print(helan_flag(numbers))
