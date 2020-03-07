#!/usr/bin/env python
# -*- coding: utf-8 -*-


def combinationSum2(nums, target):
    """
    给定一个候选数字集candidates和一个目标数值target，请找到候选子集数字加和等于目标数值的所有组合。
    注意：candidates中的每个数字最多只允许使用一次。
    :param nums: List[int]
    :param target: int
    :return: List[List[int]]
    """
    def fun(tmpNums, tmpTarget, start, path, res):
        if tmpTarget == 0 and path not in res:
            return res.append(path + [])
        for i in range(start, len(tmpNums)):
            if tmpTarget - tmpNums[i] >= 0:
                path.append(tmpNums[i])
                fun(tmpNums, tmpTarget - tmpNums[i], i + 1, path, res)
                path.pop()
    nums.sort()
    res = []
    fun(nums, target, 0, [], res)
    return res


def combinationSum2_1(candidates, target):
    candidates.sort()
    dp = [set() for _ in range(target + 1)]
    dp[0].add(())
    for candidate in candidates:
        for i in reversed(range(candidate, target + 1)):
            # 之所以要倒序，是因为如果正序的话，那么对于每次可能的for pre in dp[i - candidate]，
            # 都有可能使得dp[i].add(pre + (candidate,))执行一次，而dp[i]就有可能重复加入了candidate元素而导致错误。
            for pre in dp[i - candidate]:
                dp[i].add(pre + (candidate,))
    return list(dp[target])


if __name__ == "__main__":
    nums = [2,5,2,1,2]
    target = 5
    print(combinationSum2_1(nums, target))