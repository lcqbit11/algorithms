#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def flatten(root):
    node_list = []

    def pre_order_traveral(root):
        if root:
            node_list.append(root)
            pre_order_traveral(root.left)
            pre_order_traveral(root.right)
        
    pre_order_traveral(root)
    for i in range(1, len(node_list)):
        node, right = node_list[i-1], node_list[i]
        node.left = None
        node.right = right
    

