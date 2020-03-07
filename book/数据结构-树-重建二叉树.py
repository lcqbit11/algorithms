#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode

def before_middle_construct_tree(before_seq, middle_seq):
    """
    根据二叉树的前序遍历和中序遍历重建二叉树
    :param before_seq: List[int]
    :param middle_seq: List[int]
    :return: TreeNode
    """
    if len(before_seq)  == 0 or len(middle_seq) == 0:
        return
    root_node = TreeNode(before_seq[0])
    root_index = middle_seq.index(root_node.val)
    left_node = before_middle_construct_tree(before_seq[1:root_index + 1], middle_seq[:root_index])
    right_node = before_middle_construct_tree(before_seq[root_index + 1:], middle_seq[root_index + 1:])
    root_node.left = left_node
    root_node.right = right_node
    return root_node

def layer_traverse(root):
    from collections import deque
    node = deque()
    node.append(root)
    result = []
    while node:
        temp = node.popleft()
        result.append(temp.val)
        if temp.left:
            node.append(temp.left)
        if temp.right:
            node.append(temp.right)

    return result

if __name__ == "__main__":
    before_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middle_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    root = before_middle_construct_tree(before_seq, middle_seq)

    # root = TreeNode(1)
    # root.left = layer2_left = TreeNode(4)
    # root.right = layer2_right = TreeNode(2)
    # layer2_left.left = TreeNode(3)
    # layer2_left.right = TreeNode(6)
    print(layer_traverse(root))