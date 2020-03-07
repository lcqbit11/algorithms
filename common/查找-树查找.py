#/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode


def tree_search(root, target):
    """
    :param root: TreeNode
    :param target: int
    :return: node
    """
    if not root:
        return None
    while root:
        if target > root.val:
            root = root.right
            return tree_search(root, target)
        elif target < root.val:
            root = root.left
            return tree_search(root, target)
        else:
            return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = layer2_left = TreeNode(2)
    root.right = layer2_right = TreeNode(6)
    layer2_left.left = TreeNode(1)
    layer2_left.right = TreeNode(3)
    layer2_right.left = TreeNode(5)
    layer2_right.right = TreeNode(7)
    print(tree_search(root, 4))