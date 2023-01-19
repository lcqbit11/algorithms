#!/usr/bin/env python
# -*_ coding:utf-8 -*-

from utils.treeNodeP import TreeNodeP

def tree_node_next(root, node):
    """
    给出一个节点的中序遍历的下一个节点
    :param root: TreeNodeP
    :param node: TreeNodeP
    :return: TreeNodeP
    """
    if not node:
        return
    result = TreeNodeP(-1)
    if node.right:
        result = node.right
        while result.left:
            result = result.left
        return result
    if node.parent:
        if node.parent.left == node:
            return node.parent
        if node.parent.right == node:
            temp = node.parent
            while temp.parent:
                if temp.parent.left == temp:
                    return temp.parent
                else:
                    temp = temp.parent

    return

if __name__ == "__main__":
    root = TreeNodeP(1)
    root.left = layer2_left = TreeNodeP(4)
    layer2_left.parent = root
    root.right = layer2_right = TreeNodeP(2)
    layer2_right.parent = root
    layer2_left.left = layer3_left = TreeNodeP(3)
    layer3_left.parent = layer2_left
    layer2_left.right = layer3_right = TreeNodeP(6)
    layer3_right.parent = layer2_left

    print(tree_node_next(root, layer2_left).val)