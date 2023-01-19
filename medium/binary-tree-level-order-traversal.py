#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.treeNode import TreeNode
from collections import deque


def binary_tree_level_order_traversal(root):
    """
    层序遍历二叉树。
    先遍历第一层从左向右遍历，
    再遍历第二层从左向右遍历，
    在遍历第三层从左向右遍历，，，一直到最后一层从左向右遍历。
    :param root: TreeNode(int)
    :return: List[List[int]]
    """
    if not root:
        return []
    res = [[root.val]]
    d = deque([root])

    while d:
        tmp_val = []
        for _ in range(0, len(d)):
            tmp_node = d.popleft()
            if tmp_node.left:
                d.append(tmp_node.left)
                tmp_val.append(tmp_node.left.val)
            if tmp_node.right:
                d.append(tmp_node.right)
                tmp_val.append(tmp_node.right.val)
        if tmp_val:
            res.append(tmp_val)

    return res


def binary_tree_level_order_traversal1(root):
    if not root:
        return None
    s = [root]
    res = []
    hist_l = 0
    while len(s) > hist_l:
        tmp = []
        l = len(s)
        for i in range(hist_l, l):
            root = s[i]
            tmp.append(root.val)
            if root.left:
                s.append(root.left)
            if root.right:
                s.append(root.right)
        hist_l = l
        res.append(tmp)

    return res


def binary_tree_level_order_traversal2(root):
    if not root:
        return
    s = [root]
    res = []
    while s:
        tmp = []
        l = len(s)
        for i in range(l):
            root = s[i]
            tmp.append(root.val)
            if root.left:
                s.append(root.left)
            if root.right:
                s.append(root.right)
        del s[:l]
        res.append(tmp)
    return res


if __name__ == "__main__":
    """
            1
        4       2
    3       6
    """
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    print(binary_tree_level_order_traversal(root))