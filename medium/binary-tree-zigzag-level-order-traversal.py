#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode
from collections import deque


def binary_tree_zigzag_level_order_traversal(root):
    """
    给定一棵二叉树，返回其按层的Z字形的节点值的遍历。即从左往右遍历，下一层从右往左遍历，之后依次循环。
    :param root: TreeNode(int)
    :return: List[int]
    """
    if not root:
        return
    d = deque([root])
    res = []
    odd = True
    while d:
        level = []
        for i in range(len(d)):
            tmp = d.popleft()
            level.append(tmp.val)
            if tmp.left:
                d.append(tmp.left)
            if tmp.right:
                d.append(tmp.right)
        if level:
            if odd:
                res.append(level)
            else:
                res.append(level[::-1])
        odd = not odd

    return res


def binary_tree_zigzag_level_order_traversal1(root):
    if not root:
        return None
    s = [root]
    res = [[root.val]]
    flag = True
    odd = False
    while flag:
        flag = False
        hist_l = len(s)
        tmp = []
        for i in range(hist_l):
            root = s[i]
            if root.left:
                s.append(root.left)
                tmp.append(root.left.val)
            if root.right:
                s.append(root.right)
                tmp.append(root.right.val)
        if tmp:
            res.append(tmp if odd else tmp[::-1])
            flag = True
        odd = not odd
        s = s[hist_l:]
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    print(binary_tree_zigzag_level_order_traversal1(root))