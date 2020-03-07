#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil


def koko_eating_bananas(piles, h):
    """
    又一个包含N个元素的数组，每个元素分别表示每堆香蕉的数量，守卫离开后的H小时之内返回。
    KOKO可以决定自己吃香蕉的速度K，在每个Hour内，KOKO会选择某一堆香蕉吃并且吃掉K个香蕉，
    但是当香蕉剩余的数量少于K时，那么KOKO则把剩余的香蕉全部吃掉并且在该Hour内不再吃其他的香蕉了，
    KOKO喜欢悠闲地吃香蕉，但是又要在守卫回来之前吃完所有的香蕉，为了保证KOKO在H小时内吃完，请计算满足条件的最小的K值。
    :param piles: List[int]
    :param h: int
    :return: int
    """
    eat = lambda hour: sum(int(ceil(float(i) / hour)) for i in piles)
    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2
        if eat(mid) <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left


def koko_eating_bananas1(piles, H):
    def eat_hour(speed):
        res = 0
        for i in range(len(piles)):
            hour = piles[i] // speed
            res += hour + 1 if piles[i] - speed * hour > 0 else hour
        return res

    left, right = 1, max(piles)
    while left < right:
        mid = int((left + right) / 2)
        if eat_hour(mid) <= H:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    piles = [3,6,7,11]
    H = 8
    # piles = [11, 11, 11, 11]
    # H = 4
    print(koko_eating_bananas(piles, H))