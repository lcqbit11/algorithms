#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bestProfile(prices):
    """
    给定一个数组，数组中第i个元素表示股票在第i天的价格，如果买入股票若干天后又卖出，
    中间可以发生多次交易（买入股票1次然后卖出股票1次），请计算最大的收益。
    注意：如果你手中当前股票，那么必须要先卖出股票，才有可能下次重新买入股票。
    :param prices: List[float]
    :return maxProfiles: float
    """
    res = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i-1] > 0:
            res += prices[i] - prices[i-1]

    return res


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(bestProfile(prices))