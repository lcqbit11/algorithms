#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
# sys.path.append(BASE_DIR)
# from utils.treeNode import TreeNode, layer_traverse
# from utils.listNode import ListNode, show_list_node


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return self.subPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def subPath(self, head, node):
        if not head:
            return True
        if not node:
            return False
        if head.val != node.val:
            return False
        return self.subPath(head.next, node.left) or self.subPath(head.next, node.right)
        


        #     if not head.next:
        #         return True
        #     else:
        #         if root.left and self.isSubPath(head.next, root.left):
        #             return True
        #         if root.right and self.isSubPath(head.next, root.right):
        #             return True
        # else:
        #     if root.left and self.isSubPath(head, root.left):
        #         return True
        #     if root.right and self.isSubPath(head, root.right):
        #         return True

        # return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(2)
    layer2_left.left = TreeNode(3)
    layer2_left.right = TreeNode(6)  

    head = ListNode(1)
    # head.next = mid1 = ListNode(2)
    # mid1.next = mid2 = ListNode(5)
    head.next = None 

    solu = Solution()
    print(solu.isSubPath(head, root))


