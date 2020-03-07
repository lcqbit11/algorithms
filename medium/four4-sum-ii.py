#!/usr/bin/env python
# -*- coding: utf-8 -*-


def four4_sum_ii(A, B, C, D):
    """
    给定4个整数数组，请计算有多少个元素(i, j, k, l)，使得 A[i] + B[j] + C[k] + D[l] = 0。
    注意：假设这4个整数数组都有相同的长度。
    :param A: List[int]
    :param B: List[int]
    :param C: List[int]
    :param D: List[int]
    :return: int
    """
    res = 0
    d = {}
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] not in d:
                d[A[i] + B[j]] = 1
            else:
                d[A[i] + B[j]] += 1

    for k in range(len(C)):
        for m in range(len(D)):
            if - C[k] - D[m] in d:
                res += d[- C[k] - D[m]]

    return res


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(four4_sum_ii(A, B, C, D))