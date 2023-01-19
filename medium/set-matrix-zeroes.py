#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.printMatrix import print_matrix


def set_matrix_zeroes(matrix):
    """
    给定一个m*n的矩阵，如果一个元素为0，则将该元素所在的行和列都设置为0，就地进行设置。
    :param matrix: List[List[int]]
    :return: List[List[int]]
    """
    m = len(matrix)
    n = len(matrix[0])
    col_zero_flag = False
    for i in range(m):
        if matrix[i][0] == 0:
            col_zero_flag = True  # 判断第一列最终是否全部设置为0
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in reversed(range(m)):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col_zero_flag:
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = [
              [0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]
             ]
    # matrix = [[1,1,1],[0,1,2]]
    print_matrix(set_matrix_zeroes(matrix))