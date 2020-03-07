#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bestTimeStock1(prices):
    if not prices:
        return 0
    min_p = prices[0]
    max_diff = 0
    for i in range(len(prices)):
        min_p = min(min_p, prices[i])
        max_diff = max(max_diff, prices[i]-min_p)
    return max_diff


def bestTimeStock(prices):
    """
    给定一个数组，数组中第i个元素表示股票在第i天的价格，如果你只被允许交易一次（买入股票一次和卖出股票一次），
    请设计算法来计算最大的收益。
    :param prices: List[int]
    :return maxProfits: int
    """
    if not prices:
        return 0
    buy = -prices[0]
    sell = 0
    for i in range(1, len(prices)):
        buy = max(buy, -prices[i])
        sell = max(sell, prices[i]+buy)

    return sell


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(bestTimeStock1(prices))