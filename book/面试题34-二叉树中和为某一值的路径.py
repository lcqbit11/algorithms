#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.treeNode import TreeNode


def find_path(root, target):
    """
    输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
    注意：从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
    :param root: TreeNode(int)
    :return: List[int]
    """
    def find_(root, target, path, cur_sum, res):
        cur_sum += root.val
        path.append(root.val)
        is_leaf = not root.left and not root.right
        if cur_sum == target and is_leaf:
            res.append(path + [])
        if root.left:
            find_(root.left, target, path, cur_sum, res)
        if root.right:
            find_(root.right, target, path, cur_sum, res)
        path.pop()  # 跳出本次递归之前需要复原path
        cur_sum -= root.val  # 跳出本次递归之前需要复原cur_sum

    if not root:
        return
    res = []
    find_(root, target, [], 0, res)

    return res


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = layer2_left = TreeNode(5)
    root.right = layer2_right = TreeNode(12)
    layer2_left.left = TreeNode(4)
    layer2_left.right = TreeNode(7)

    print(find_path(root, 22))