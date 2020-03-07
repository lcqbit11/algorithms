#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.treeNode import TreeNode


def is_sort_binary_tree(root):
    """
    给定一棵二叉树，判断其是否是排序二叉树。
    对于根节点，如何其存在左子树，那么左子树的所有节点均不大于根节点大小，
    如果其存在右子树，那么右子树的所有节点均不小于根节点大小，这样的树称为排序二叉树。
    :param head: TreeNode(int)
    :return: bool
    """
    res = []
    s = []
    while root or s:  # 根据二叉树的中序遍历结果来判断，即当前遍历的节点数值是否始终不小于上次遍历的节点数值
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        res.append(root.val)
        if len(res) >= 2 and res[-2] > res[-1]:
            return False
        root = root.right
    return True


if __name__ == "__main__":
    """
                4
            2       6
        1       3
        """
    root = TreeNode(4)
    root.left = layer2_left = TreeNode(2)
    root.right = layer2_right = TreeNode(6)
    layer2_left.left = TreeNode(1)
    layer2_left.right = TreeNode(3)

    print(is_sort_binary_tree(root))