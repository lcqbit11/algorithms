#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode
from collections import deque

def tree_bfs(root):
    """
    树结构的广度优先遍历（应用到二叉树上来看，其实就是层序遍历）
    :param root:
    :return:
    """
    res = []
    q = deque()
    if root:
        q.append(root)
    while q:
        root = q.popleft()
        res.append(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
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

    print(tree_bfs(root))