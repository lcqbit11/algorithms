#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from utils.treeNode import TreeNode


def binary_tree_post_order_traversal2(root):
    res = []
    s =[]
    while root or s:
        while root:
            s.append(root)
            if root.left:
                root = root.left
            else:
                root = root.right
        root = s.pop()
        res.append(root.val)
        if len(s) > 0 and s[-1].left == root:
            root = s[-1].right
        else:
            root = None
    return res


def binary_tree_post_order_traversal1(root, res):
    if root:
        binary_tree_post_order_traversal1(root.left, res)
        binary_tree_post_order_traversal1(root.right, res)
        res.append(root.val)


def binary_tree_post_order_traversal(root):
    """
    二叉树的后序遍历
    :param root: TreeNode
    :return: List[int]
    """
    if not root:
        return []
    res = []
    stack = []
    stack.append((1, root))
    while stack:
        p = stack.pop()
        if not p[1]:
            continue
        if p[0] == 0:
            res.append(p[1].val)
        else:
            stack.extend([(0, p[1]), (1, p[1].right), (1, p[1].left)])
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

    # print(binary_tree_post_order_traversal(root))
    # res = []
    # binary_tree_post_order_traversal1(root, res)
    # print(res)
    print(binary_tree_post_order_traversal2(root))