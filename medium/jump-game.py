#!/usr/bin/env python
# -*- coding: utf-8 -*-


def jump_game(nums):
    """
    给定一个非负整数数组，每个元素表示在当前位置上k可以跳动的最大长度，
    初始位置是在数组的第一个位置上，请判断是否能够达到最后一个位置。
    :param nums: List[int]
    :return: bool
    """
    maxLoc = 0  # 当前能到达的最大位置下标
    for i in range(len(nums)):
        if maxLoc < i:  # 历史能到达的最大位置小于当前的位置
            return False
        maxLoc = max(maxLoc, i + nums[i])
    return True


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    # nums = [3,2,1,2,4]
    print(jump_game(nums))