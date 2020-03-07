#!/usr/bin/emv python
# -*- coding: utf-8 -*-
from lib.treeNode import TreeNode


def has_sub_tree(root1, root2):
    """
    输入两棵二叉树T1和T2，判断T2是不是T1的子结构。
    :param root1: TreeNode(int)
    :param root2: TreeNode(int)
    :return: bool
    """
    def is_sub_tree(root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return is_sub_tree(root1.left, root2.left) and is_sub_tree(root1.right, root2.right)

    res = False
    if root1 and root2:
        if root1.val == root2.val:
            res = is_sub_tree(root1, root2)
        if not res:
            res = has_sub_tree(root1.left, root2)
        if not res:
            res = has_sub_tree(root1.left, root2)
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    root1 = TreeNode(1)
    root1.left = layer12_left = TreeNode(4)
    root1.right = layer12_right = TreeNode(3)

    print(has_sub_tree(root, root1))

