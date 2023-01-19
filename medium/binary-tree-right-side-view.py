#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.treeNode import TreeNode
from collections import deque


def binary_tree_right_side_view(root):
    """
    对于一棵二叉树，从右边看它，输出你能看到的每一层的节点，从上往下输出。
    :param root: TreeNode(int)
    :return: List[int]
    """
    if not root:
        return []
    res = []
    d = deque([root])
    res.append(root.val)
    while d:
        nums = []
        l = len(d)
        for _ in range(0, l):
            tmp = d.popleft()
            if tmp.left:
                d.append(tmp.left)
                nums.append(tmp.left.val)
            if tmp.right:
                d.append(tmp.right)
                nums.append(tmp.right.val)
        if nums:
            res.append(nums[-1])

    return res


def binary_tree_right_side_view1(root):
    if not root:
        return None
    s = [root]
    res = [root.val]
    while s:
        tmp = []
        hist_l = len(s)
        for i in range(hist_l):
            root = s[i]
            if root.left:
                s.append(root.left)
                tmp.append(root.left.val)
            if root.right:
                s.append(root.right)
                tmp.append(root.right.val)
        s = s[hist_l:]
        if tmp:
            res.append(tmp[-1])
    return res


def binary_tree_right_side_view2(root):
    if not root:
        return
    res = []
    s = [root]
    while s:
        l = len(s)
        for i in range(l):
            root = s[i]
            if i == l-1:
                res.append(root.val)
            if root.left:
                s.append(root.left)
            if root.right:
                s.append(root.right)
        del s[:l]
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

    print(binary_tree_right_side_view2(root))