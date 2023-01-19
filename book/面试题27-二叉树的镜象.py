#!/usr/bin/emv python
# -*- coding: utf-8 -*-
from utils.treeNode import TreeNode, layer_traverse


def tree_mirror(root):
    """
    :param root: TreeNode(int)
    :return: TreeNode(int)
    """
    if not root:
        return root
    left_mirror = tree_mirror(root.left)
    right_mirror = tree_mirror(root.right)
    root.left = right_mirror
    root.right = left_mirror

    return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    print(layer_traverse(tree_mirror(root)))



