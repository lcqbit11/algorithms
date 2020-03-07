#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode

def tree_dfs(root):
    """
    树结构的深度优先遍历（应用到二叉树上来看，其实就是前序遍历）
    :param root:
    :return:
    """
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

    print(tree_dfs(root))