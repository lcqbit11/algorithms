#!/usr/bin/env python
# -*- coding: utf-8 -*-


def super_egg_drop(K, N):
    """
    给定K个鸡蛋，并且可以使用从1到N的共N层楼的建筑。每个鸡蛋都是一样的，如果一个鸡蛋碎了，你就不能把它再次扔到了。
    其中存在某一层楼F，0<=F<=N，当你在F层以上扔掉鸡蛋时，鸡蛋就会破碎；当你在F及F层以下扔掉鸡蛋时，鸡蛋不会破碎。
    每移动到一层楼x（0<=x<=N），如果你还有完整的鸡蛋的话，你都可以扔掉一个鸡蛋并观察其是否破碎，你需要通过这种确定F值大小。
    那么你至少需要多少次移动才能确定F值大小？
    :param K: int
    :param N: int
    :return: int
    参考 https://blog.csdn.net/qq_35170267/article/details/84330662
        https://blog.csdn.net/Evildoer_llc/article/details/88145864
    """
    dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]  # 表示能测出的最大层数

    for i in range(1, K + 1):  # 鸡蛋
        for j in range(1, N + 1):  # 移动次数
            # dp[i - 1][j - 1]表示本次扔之前已经确定的楼层数量，dp[i][j - 1]表示本次扔之后确定的楼层数量
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1
            if dp[K][j] >= N:  # 测出层数流程结束时，测出的层数为楼层最大值N，肯定是要测出来才行（即找到分界点F楼层）
                return j
    return N


def super_egg_drop1(K, N):
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    for t in range(1, N + 1):
        dp[1][t] = t

    for i in range(2, K + 1):
        for j in range(1, N + 1):
            dp[i][j] = j
            left, right = 1, j
            while left < right:
                mid = int((left + right) / 2)
                if dp[i - 1][mid - 1] < dp[i][j - mid]:
                    left = mid + 1
                else:
                    right = mid
            dp[i][j] = min(dp[i][j], max(dp[i - 1][right - 1], dp[i][j - right]) + 1)

    return dp[K][N]


def super_egg_drop2(K, N):
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    for t in range(1, N + 1):
        dp[1][t] = t

    for i in range(2, K + 1):
        s = 1
        for j in range(1, N + 1):
            dp[i][j] = j
            while s < j and dp[i - 1][s - 1] < dp[i][j - s]:
                s += 1
            dp[i][j] = min(dp[i][j], max(dp[i - 1][s - 1], dp[i][j - s]) + 1)

    return dp[K][N]


if __name__ == "__main__":
    K = 2
    N = 6
    print(super_egg_drop(K, N))