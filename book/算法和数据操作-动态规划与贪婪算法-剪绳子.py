#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cut_rope(l):
    """
    动态规划-剪绳子
    :param l: int
    :return: int
    """
    if l < 2:
        return 0
    if l == 2:
        return 1
    if l == 3:
        return 2

    cnt = int(l/3)
    if l-cnt*3 == 1:
        cnt -= 1
    power_cnt = int((l-cnt*3)/2)
    return pow(3, cnt)*pow(2, power_cnt)


    # if l < 2:
    #     return 0
    # if l == 2:
    #     return 1
    # if l == 3:
    #     return 2
    # product = [0] * (l+1)
    # product[0] = 0
    # product[1] = 1
    # product[2] = 2
    # product[3] = 3
    # for i in range(4, l+1):
    #     max_result = 0
    #     for j in range(1, int(i/2)+1):
    #         temp = product[j]*product[i-j]
    #         if max_result < temp:
    #             max_result = temp
    #     product[i] = max_result
    # return product[l]

if __name__ == "__main__":
    l = 9
    print(cut_rope(l))