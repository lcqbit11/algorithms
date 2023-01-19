#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.treeNode import TreeNode


def two_sum_iv_input_bst(root, k):
    """
    给定一个二叉搜索树和一个目标值，如果在树中存在两个元素加和等于目标值则返回true，
    否则返回false
    :param root: TreeNode(int)
    :return: bool
    """
    nums = []
    s = []
    while s or root:  # 中序遍历
        while root:
            s.append(root)
            root = root.left
        if s:
            root = s.pop()
            nums.append(root.val)
        root = root.right
    l = len(nums)
    low, high = 0, l - 1
    while low < high:
        if nums[low] + nums[high] > k:
            high -= 1
        elif nums[low] + nums[high] < k:
            low += 1
        else:
            return True
    return False


if __name__ == "__main__":
    """
         5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 9
    """
    root = TreeNode(5)
    root.left = layer2_left = TreeNode(3)
    root.right = layer2_right = TreeNode(6)
    layer2_left.left = TreeNode(2)
    layer2_left.right = TreeNode(4)
    layer2_right.right = TreeNode(7)

    target = 9

    print(two_sum_iv_input_bst(root, k=target))



