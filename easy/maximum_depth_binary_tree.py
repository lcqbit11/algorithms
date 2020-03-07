#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.treeNode import TreeNode


def maximum_depth_binary_tree(root):
    """
    找出二叉树的最大深度
    :param root: TreeNode
    :return: int
    """
    if not root:
        return 0
    return max(maximum_depth_binary_tree(root.left)+1, maximum_depth_binary_tree(root.right)+1)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = layer3_left = TreeNode(3)
    layer2_left.right = layer3_right = TreeNode(6)
    layer3_right.left = layer4_left = TreeNode(7)

    print(maximum_depth_binary_tree(root))