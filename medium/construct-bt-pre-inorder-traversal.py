#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.treeNode import TreeNode, layer_traverse


def construct_bt_preorder_inorder_traversal(preorder, inorder):
    """
    给定树的前序遍历和中序遍历，请构建原来的二叉树。假设不存在重复的元素。
    提示：
    前序遍历的特点是第一个元素一定是根节点；
    中序遍历的根节点元素左边的元素一定都是左子树的节点，根节点元素右边的元素一定都是右子树的节点
    :param preorder: List[int]
    :param inorder: List[int]
    :return: TreeNode(int)
    """
    def build1(preorder, inorder):
        if not preorder:
            return None
        if len(preorder) <= 1:
            return TreeNode(preorder[0])
        root_node = preorder[0]
        root = TreeNode(root_node)
        for i in range(len(inorder)):
            if root_node == inorder[i]:
                inorder_root_node_index = i
                break

        root.left = construct_bt_preorder_inorder_traversal(preorder[1:inorder_root_node_index+1], inorder[:inorder_root_node_index])
        root.right = construct_bt_preorder_inorder_traversal(preorder[inorder_root_node_index+1:], inorder[inorder_root_node_index+1:])

        return root

    return build1(preorder, inorder)


def construct_bt_preorder_inorder_traversal1(preorder, inorder):
    def build1(preorder, inorder):
        if not preorder:
            return None
        if len(preorder) <= 1:
            return TreeNode(preorder[0])
        root_node = preorder[0]
        root = TreeNode(root_node)
        for i in range(len(inorder)):
            if root_node == inorder[i]:
                inorder_root_node_index = i
                break

        root.left = build1(preorder[1:inorder_root_node_index+1], inorder[:inorder_root_node_index])
        root.right = build1(preorder[inorder_root_node_index+1:], inorder[inorder_root_node_index+1:])

        return root

    return build1(preorder, inorder)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    # preorder = [3, 2, 1, 4]
    # inorder = [1, 2, 3, 4]

    root = construct_bt_preorder_inorder_traversal1(preorder, inorder)

    print(layer_traverse(root))




