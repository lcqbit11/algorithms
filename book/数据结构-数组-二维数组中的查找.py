#!/usr/bin/env python
# -*- coding: utf-8 -*-

def search_from_2d_array(numbers, target):
    """
    :param numbers: List[List[int]]
    :return: bool
    """
    l_row = len(numbers)
    l_col = len(numbers[0])
    for i in reversed(range(0, l_row)):
        for j in range(0, l_col):
            if target > numbers[i][j]:
                j += 1
            elif target < numbers[i][j]:
                break
            else:
                return True
    return False

if __name__ == "__main__":
    numbers = [
        [1, 2, 8, 9],
        [2, 3, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    print(search_from_2d_array(numbers, 9))