#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.treeNode import TreeNode


def invertTree(root):
    """
    翻转一棵二叉树
    :param root: TreeNode(int)
    :return: TreeNode(int)
    """
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


def layerTraverse(root):
    node_a = []
    if root:
        node_a.append(root)
    while node_a:
        root = node_a.pop(0)
        print(root.val)
        if root.left:
            node_a.append(root.left)
        if root.right:
            node_a.append(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(2)
    root.right = layer2_right = TreeNode(3)
    layer2_left.left = layer31_left = TreeNode(4)
    layer2_left.right = layer31_right = TreeNode(5)
    layer2_right.left = layer32_left = TreeNode(6)
    layer2_right.right = layer32_right = TreeNode(7)

    layerTraverse(root)
    invertTree(root)
    print('\n')
    layerTraverse(root)


