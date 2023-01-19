#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.treeNode import TreeNode


def binary_tree_pre_order_traversal2(root):
    res = []
    s = []
    if root:
        s.append(root)
    while s:
        root = s.pop()
        res.append(root.val)
        if root.right:
            s.append(root.right)
        if root.left:
            s.append(root.left)

    return res


def binary_tree_pre_order_traversal1(root, res):
    if root:
        res.append(root.val)
        binary_tree_pre_order_traversal1(root.left, res)
        binary_tree_pre_order_traversal1(root.right, res)


def binary_tree_pre_order_traversal(root):
    """
    给定一棵树，返回其前序遍历的结点的数值。
    :param root: TreeNode(int)
    :return: List[int]
    """
    res = []
    tmp = [(1, root)]
    while tmp:
        p = tmp.pop()
        if not p[1]:
            continue

        if p[0]:
            tmp.extend([(1, p[1].right), (1, p[1].left), (0, p[1])])
        else:
            res.append(p[1].val)
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

    # print(binary_tree_pre_order_traversal(root))
    # res = []
    # binary_tree_pre_order_traversal1(root, res)
    # print(res)
    print(binary_tree_pre_order_traversal2(root))