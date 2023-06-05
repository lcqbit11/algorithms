#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    经典背包问题：
    一个容量为 T 的背包，和一些物品。这些物品分别有两个属性，体积 w 和价值 v，每种物品只有一个。
    所有物品体积数组 weights 和价值数组 values。要求用这个背包装下价值尽可能多的物品，求该最大价值，背包可以不被装满。
    注：
    0-1背包问题：在最优解中，每个物品只有两种可能的情况，即在背包中或者不在背包中（背包中的该物品数为0或1），因此称为0-1背包问题。

    步骤1：找子问题。子问题必然是和物品有关的，对于每一个物品，有两种结果：能装下或者不能装下。
    步骤2：确定状态。状态对应的值即为背包容量为j时，求前i个物品所能达到最大价值，设为dp[i][j]。初始时，dp[0][j](0<=j<=T)为0，没有物品也就没有价值。
    步骤3：确定状态转移方程。第i个物品的体积为w,价值为v，则状态转移方程为：
                        j<w，dp[i][j] = dp[i-1][j] //背包装不下该物品，最大价值不变；
                        j>=w, dp[i][j] = max(dp[i-1][j-weights[i]] + values[i], dp[i-1][j]) //dp[i-1][j-weights[i]]表示不放入第i个物体所需要的体积大小时的价值，然后再放入物体i在就是共i个物体总体积为j时的价值；dp[i-1][j]表示不放入该物品时同样需要体积j时的最大价值，这两种情况下进行对比，取较大值即可。
"""


def carry_bag(T, weights, values):
    """
    :param T: float
    :param weights: List[float]
    :param values: List[float]
    :return: float
    """
    if not weights or not values:
        return 0
    num = len(weights)
    dp = [[0] * (T + 1) for _ in range(num+1)]
    # 第1个物品为weights[0],values[0],,,第i个物品为weights[i-1],values[-1]
    # 第1个物品在容量j时候的最优解为dp[1][j],,,第i个物品在容量j时候的最优解为dp[i][j]
    for i in range(1, num+1):  # i 表示第i个物品
        for j in reversed(range(1, T+1)):  # j 表示背包总的容量大小（即T的大小）。j 是指背包总的容量，包括已经占用的容量和未占用的容量
                                           # j 不是指背包当前剩余的空间容量大小。
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[num][T]


if __name__ == "__main__":
    T = 5
    weights = [1, 2, 3, 2]
    values = [3, 5, 2, 1]
    print(carry_bag(T, weights, values))