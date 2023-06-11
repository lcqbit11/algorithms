#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#

# from utils.listNode import ListNode, generate_node_list, show_list_node


from threading import local


def isValidBST(root):
    pre_value = -float('inf')

    def backtrack(root):
        nonlocal pre_value
        if not root:
            return True
    
        if not backtrack(root.left):
            return False
        
        if root.val <= pre_value:
            return False
        
        pre_value = root.val

        return backtrack(root.right)

    return backtrack(root)


# root = generate_node_list([2, 1, 3])
# show_list_node(root)
