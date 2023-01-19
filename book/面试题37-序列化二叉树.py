#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from utils.treeNode import TreeNode, layer_traverse

"""
参考：https://www.cnblogs.com/ansang/p/11907595.html
"""


class Solution(object):
    def serialize(self, root):
        if not root:
            return 'null'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, s):
        def deserialize_tree(s):
            if not s:
                return
            val = s.pop(0)
            root = None
            if val != 'null':
                root = TreeNode(val)
                root.left = deserialize_tree(s)
                root.right = deserialize_tree(s)
            return root

        vallist = s.split(',')
        return deserialize_tree(vallist)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)
    
    solu = Solution()
    s = solu.serialize(root)
    res = solu.deserialize(s)
    print(s)
    print(layer_traverse(res))