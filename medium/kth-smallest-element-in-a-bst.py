#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode


def kth_smallest_element_in_a_bst(root, k):
    """
    ，请返回树中第k小的元素。
    :给定一个搜索二叉树root: TreeNode(float)
    :return: float
    """
    # nums = []
    # res = 0
    # def fun(head, index):
    #     if not head:
    #         pass
    #     if head.left:
    #         fun(head.left, index)
    #     nums.append(head.val)
    #     index += 1
    #     print(index)
    #     if index == k:
    #         res = head.val
    #     if head.right:
    #         fun(head.right, index)
    #
    # fun(root, 0)
    #
    # return res

    # nums = []
    stack = [(1, root)]
    index = 0
    while stack:
        p = stack.pop()
        if not p[1]:
            continue
        if p[0] != 0:
            stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)])
        else:
            # nums.append(p[1].val)
            index += 1
            if index == k:
                return p[1].val

    return


def kth_smallest_element_in_a_bst1(root, k):
    if not root:
        return None
    s = []
    index = 0
    # 按照二叉树中序遍历方式遍历到第k个节点对应的值即为第k小的元素
    while root or s:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        index += 1
        if index == k:
            return root.val
        root = root.right
    return None


if __name__ == "__main__":
    # root = TreeNode(1)
    # root.left = layer2_left = TreeNode(4)
    # root.right = layer2_right = TreeNode(2)
    # layer2_left.left = TreeNode(3)
    # layer2_left.right = TreeNode(6)

    root = TreeNode(4)
    root.left = layer2_left = TreeNode(2)
    root.right = layer2_right = TreeNode(6)
    layer2_left.left = TreeNode(1)
    layer2_left.right = TreeNode(3)

    k = 3

    print(kth_smallest_element_in_a_bst1(root, k))