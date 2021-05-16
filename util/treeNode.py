#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
"""
            1
        4       2
    3       6

root = TreeNode(1)
root.left = layer2_left = TreeNode(4)
root.right = layer2_right = TreeNode(2)
layer2_left.left = TreeNode(3)
layer2_left.right = TreeNode(6)
"""

"""
请加入下面代码开头：
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def layer_traverse(root):
    s = [root]
    res = []
    while s:
        root = s.pop(0)
        res.append(root.val)
        if root.left:
            s.append(root.left)
        if root.right:
            s.append(root.right)

    return res