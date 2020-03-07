#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.treeNode import TreeNode


def tree_in_order_traversal2(root):
    res = []
    s = []
    while root or s:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        res.append(root.val)
        root = root.right
    return res


def tree_in_order_traversal1(root, res):
    if root:
        tree_in_order_traversal1(root.left, res)
        res.append(root.val)
        tree_in_order_traversal1(root.right, res)


def tree_in_order_traversal(root):
    """
    二叉树的中序遍历
    :param root: TreeNode
    :return: List
    """
    # 递归方式解法
    # def fun(root, tmpNums):
    #     if root == None:
    #         return
    #     fun(root.left, tmpNums)
    #     tmpNums.append(root.val)
    #     fun(root.right, tmpNums)
    #
    # nums = []
    # fun(root, nums)
    #
    # return nums

    # 非递归方式解法，父亲节点的元组中第一个元素为0，孩子节点的元组中第一个元素为1
    res = []
    s = [(1, root)] # 0表示不可以往下遍历，1表示可以往下继续遍历
    while s:
      p = s.pop()
      if not p[1]:  # 判断某个节点为空
          continue
      if p[0]:  # 判断为子节点的话，就继续往栈里面放数据
          s.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)])
      else:  # 判断为主节点的话，就说明其左节点已经为空了，那么该父节点可以输出到数组中了
          res.append(p[1].val)
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

    # print(tree_in_order_traversal(root))
    # res = []
    # tree_in_order_traversal1(root, res)
    # print(res)
    print(tree_in_order_traversal(root))