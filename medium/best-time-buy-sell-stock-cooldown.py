#!/usr/bin/env python
# -*- coding: utf-8 -*-


def best_time_to_buy_sell_stock_cooldown(nums):
    """
    数组中的数值表示股票的价格，遵循的规则是：
    1.在下次购入之前必须要把当前的卖出去才行;
    2.买出去之后的第二天不能再次买入，即至少要冷却一天
    :param nums: List[float]
    :return: float
    解法：以数组中的当前元素作为结尾，
    计算以当前元素作为结尾的买入价格的最大收益，计算以当前元素作为结尾的卖出价格的最大收益。
    """
    if not any(nums) or len(nums) == 1:
        return 0
    buy = [0] * len(nums)
    sell = [0] * len(nums)
    buy[0] = -nums[0]
    buy[1] = max(buy[0], -nums[1])
    sell[0] = 0
    sell[1] = max(sell[0], nums[1]+buy[0])
    for i in range(2, len(nums)):
        buy[i] = max(buy[i-1], sell[i-2] - nums[i])  # 表示在第i天及之前的最后一个操作是买：上次买入的话则buy[i-1]，本次买入的话(sell[i-2] - nums[i])
        sell[i] = max(sell[i-1], buy[i-1] + nums[i])  # 表示在第i天及之前的最后一个操作是卖：上次卖出的话则sell[i-1]，本次卖出的话则(buy[i-1] + nums[i])
    return sell[-1]


def best_time_to_buy_sell_stock_cooldown1(nums):
    if not any(nums) or len(nums) == 1:
        return 0
    pre_buy = -nums[0]
    buy = max(pre_buy, -nums[1])
    pre_sell = 0
    sell = max(pre_sell, pre_buy + nums[1])
    for i in range(2, len(nums)):
        pre_buy = buy
        buy = max(pre_buy, pre_sell - nums[i])
        pre_sell = sell
        sell = max(pre_sell, pre_buy + nums[i])
    return sell


if __name__ == "__main__":
    nums = [1,2,3,0,2]
    print(best_time_to_buy_sell_stock_cooldown1(nums))