#!/usr/bin/env python
# -*- coding: utf-8 -*-

def robotic_domain(m, n, k):
    """
    :param m: int
    :param n: int
    :param k: int
    :return: int
    """
    def get_bit_sum(m):
        sum = 0
        while m > 0:
            sum += int(m % 10)
            m = int(m / 10)
        return sum

    def check(k, rows, cols, row, col, visited):
        if row<rows and col<cols and row>=0 and col>=0 and get_bit_sum(row)+get_bit_sum(col)<=k and not visited[row][col]:
            return True
        return False

    def count_numbers(k, rows, cols, row, col, visited):
        count_cnt = 0
        if check(k, rows, cols, row, col, visited):
            visited[row][col] = True
            count_cnt = 1 + count_numbers(k, rows, cols, row, col, visited) + count_numbers(k, rows, cols, row-1, col, visited) + count_numbers(k, rows, cols, row, col-1, visited) + count_numbers(k, rows, cols, row+1, col, visited) + count_numbers(k, rows, cols, row, col+1, visited)
        return count_cnt

    if k<=0 and m<=0 and n<=0:
        return 0
    visited = [[False]*n for i in range(m)]
    return count_numbers(k, m, n, 0, 0, visited)

if __name__ == "__main__":
    m, n, k = 3, 3, 3
    print(robotic_domain(m, n, k))