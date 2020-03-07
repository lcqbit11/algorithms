#!/usr/bin/env python
# -*- coding: utf-8 -*-


def coin_change(coins, amount):
    """
    给定不同面值的硬币(假设每种面值的硬币都有无限多个)和一个总金额，请计算出组成该总金额所需要硬币的最少数量。如果无法组成，则返回-1。
    :param coins: List[int]
    :param amount: int
    :return: int
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coin_change(coins, amount))