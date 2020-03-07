#!/usr/bin/env python
# -*- coding: utf-8 -*-

def matrix_path(matrix, s):
    """
    :param matrix: List[List[int]]
    :param s: str
    :return: bool
    """
    def new_matrix(m, row, col):
        matrix = [[0] * len(m[0]) for k in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if row == i and col == j:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = m[i][j]
        return matrix

    def has_path(matrix, row, col, i, j, s):
        if len(s) == 0:
            return True
        is_path = False
        if i >= 0 and i < row and j >= 0 and j < col and matrix[i][j] == s[0]:
            matrix = new_matrix(matrix, i, j)
            is_path = has_path(matrix, row, col, i+1, j, s[1:]) or has_path(matrix, row, col, i, j+1, s[1:]) or has_path(matrix, row, col, i-1, j, s[1:]) or has_path(matrix, row, col, i, j-1, s[1:])
        return is_path

    row = len(matrix)
    col = len(matrix[0])
    length = len(s)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == s[0]:
                if has_path(matrix, row, col, i, j, s):
                    return True
    return False

if __name__ == "__main__":
    matrix = [['a', 'b', 't', 'g'],
              ['c', 'f', 'c', 's'],
              ['j', 'd', 'e', 'h']]
    s = "bfce"
    print(matrix_path(matrix, s))