#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
from utils.treeNode import TreeNode


class Solution(object):
    res = float("-inf")
    def binary_tree_maximum_path_sum(self, root):
        """
        给定一个二叉树的根节点，计算该树中由父子节点连接成的路径的和最大
        :param root: TreeNode(int)
        :return: int
        """
        def helper(node):  # 计算以node为路径的边界节点的最大的路径之和
            if not node:
                return 0
            left = max(helper(node.left), 0)  # 如果有加和为负值的左路径，就直接省略了
            right = max(helper(node.right), 0)  # 如果有加和为负值的右路径，就直接省略了
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val

        helper(root)
        return self.res


if __name__ == "__main__":
    """
                    -10
                20       9
             15    7
    上面的和最大路径就是 15-20-7，最大和为42
    """
    root = TreeNode(-10)
    root.left = layer2_left = TreeNode(20)
    root.right = layer2_right = TreeNode(9)
    layer2_left.left = layer3_left1 = TreeNode(15)
    layer2_left.right = layer3_right1 = TreeNode(7)
    layer2_right.left = None
    layer2_right.right = None
    layer3_left1.left = None
    layer3_left1.right = None
    layer3_right1.left = None
    layer3_right1.right = None

    solu = Solution()
    print(solu.binary_tree_maximum_path_sum(root))