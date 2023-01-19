#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.treeNode import TreeNode, layer_traverse


def construct_bt_inorder_postorder_traversal(inorder, postorder):
    """
    给定二叉树的中序遍历和后序遍历数组，请重构这棵二叉树
    :param inorder: List[int]
    :param postorder: List[int]
    :return: TreeNode(int)
    """
    def build1(inorder, postorder):
        if not inorder:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            postorder_root_val = postorder[-1]
            root = TreeNode(postorder_root_val)
            for i in range(len(inorder)):
                if postorder_root_val == inorder[i]:
                    inorder_root_index = i
                    break
            if inorder_root_index == 0:
                root.left = None
                root.right = build1(inorder[1:], postorder[:-1])
            elif inorder_root_index == len(inorder) - 1:
                root.left = build1(inorder[:-1], postorder[:-1])
                root.right = None
            else:
                root.left = build1(inorder[:inorder_root_index], postorder[:inorder_root_index])
                root.right = build1(inorder[inorder_root_index + 1:], postorder[inorder_root_index:-1])

        return root

    def build2(inorder, postorder):
        if not inorder:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            postorder_root_val = postorder[-1]
            root = TreeNode(postorder_root_val)
            for i in range(len(inorder)):
                if postorder_root_val == inorder[i]:
                    inorder_root_index = i
                    break
            root.left = build2(inorder[:inorder_root_index], postorder[:inorder_root_index])
            root.right = build2(inorder[inorder_root_index + 1:], postorder[inorder_root_index:-1])
        return root

    return build2(inorder, postorder)


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    res = construct_bt_inorder_postorder_traversal(inorder, postorder)

    print(layer_traverse(res))