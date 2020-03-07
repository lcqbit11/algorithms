#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from lib.treeNode import TreeNode


def binary_tree_transform(root):
    """
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的节点，只能调整树中节点指针的方向。
    注意：在二叉树中，每个节点都有两个指向子节点的指针。在双向链表中，每个节点也有两个指针，分别指向前一个节点和后一个节点。
    :param root: TreeNode(int)
    :return: TreeNode(int)
    """
    if not root:
        return
    s = []
    pre = None
    head = None
    while s or root:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        if not head:
            head = root
        if pre:
            pre.right = root
            root.left = pre
        pre = root
        root = root.right
    pre.right = head
    head.left = pre
    
    return head


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)

    res = binary_tree_transform(root)
    index = 1
    while res and index < 6:
        print(res.val)
        res = res.right
        index += 1