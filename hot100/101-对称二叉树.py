#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。#


def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        if (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left):
            return True
        
        return False

    return isMirror(root, root)
