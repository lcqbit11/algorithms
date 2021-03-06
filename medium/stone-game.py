#!/usr/bin/env python
# -*- coding: utf-8 -*-


def stone_game(piles):
    """
    A和B两人在玩石头游戏，有偶数堆石子，每堆石子的数量为piles[i]，游戏的目标是获得石子数量最多的人获胜，
    石子的总数量是奇数，所有总会有胜出的人。
    A得到第一堆石子，之后两人轮流，每个人可以得到当前剩余堆石子的第一堆或者最后一堆，直到没有石子剩余为止，
    此时获得石子数量最多的人取胜。
    假设A和B两人的玩法都是最优的，当且仅当A取胜时，返回True。
    请判断返回结果是True还是False。
    题目分析：假设条件为A可以做到玩法最优，因为有偶数堆石子，所以所有的奇数堆加和和所有的偶数堆加和相比，一定是一个多一个少，
    那么A可以实现计算出来是奇数堆加和大一些还是偶数堆加和大一些，假设所有奇数堆加和大一些，那么A可以先取第一堆，此时B只能取第二堆或者
    最后一堆(也是第偶数堆)，即B只能取第偶数堆，不管B是取第二堆或者最后一堆，下一次A一定可以取到第奇数堆，这样循环下去，A每次都能取到
    第奇数堆，而B每次都不得不取第偶数堆，这样的还A一定能赢得比赛。
    :param piles: list[int]
    :return: bool
    """
    return True


if __name__ == "__main__":
    nums = [5, 3, 4, 5]
    print(stone_game(nums))