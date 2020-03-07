#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.treeNode import TreeNode


def lowest_common_ancestor_binary_tree(root, p, q):
    """
    给定一棵二叉树，请找到树中的两个节点p,q的最低公共祖先（LCA）。允许一个节点成为它自己的后代节点。
    :param root: TreeNode(int)
    :param p: TreeNode(int)
    :param q: TreeNode(int)
    :return: TreeNode(int)
    """
    def fun(head, p1, q1):
        if not head:
            return head

        left = fun(head.left, p1, q1)
        right = fun(head.right, p1, q1)

        if left and right:
            return head

        if head == p1 or head == q1:
            return head

        if left:
            return left

        if right:
            return right

        return None

    return fun(root, p, q)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    p = root.left.left
    q = root.right

    print(lowest_common_ancestor_binary_tree(root, p, q).val)