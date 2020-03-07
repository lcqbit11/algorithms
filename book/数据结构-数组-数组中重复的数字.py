#!/usr/bin/env python
# -*- coding: utf-8 -*-

def duplication_in_array(numbers):
    """
    :param numbers: List[int]
    :return: int
    """
    i = 0
    while i < len(numbers):
        if i != numbers[i]:
            if numbers[numbers[i]] != numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
            else:
                return numbers[i]
        else:
            i += 1

if __name__ == "__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    print(duplication_in_array(numbers))