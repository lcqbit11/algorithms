#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def maxDepth(root):
    def depth(root):
        if not root:
            return 0
    
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        return 1+max(left_depth, right_depth)
    return depth(root)
