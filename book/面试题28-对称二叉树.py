#!/usr/bin/emv python
# -*- coding: utf-8 -*-
from lib.treeNode import TreeNode, layer_traverse


def symmetrical_tree(root):
    """
    判断一棵树是否是对称二叉树？
    解题思路：如果一棵树和它的镜像是完全一样的，那么这棵树一定是对称二叉树
    :param root:
    :return:
    """
    # Solution1
    # def tree_mirror(root):
    #     if not root:
    #         return root
    #     left_mirror = tree_mirror(root.left)
    #     right_mirror = tree_mirror(root.right)
    #     root.left = right_mirror
    #     root.right = left_mirror
    #     return root
    #
    # def same_tree(root1, root2):
    #     if not root1 and not root2:
    #         return True
    #     elif not root1:
    #         return False
    #     elif not root2:
    #         return False
    #     if root1.val != root2.val:
    #         return False
    #     if root1.val == root2.val:
    #         return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)
    #
    # mirror_root = tree_mirror(root)
    # return same_tree(root, mirror_root)

    # Solution2
    # def pre_traverse(root):
    #     res = []
    #     s = []
    #     while root or s:
    #         while root:
    #             s.append(root)
    #             res.append(root.val)
    #             root = root.left
    #         if s:
    #             root = s.pop()
    #             root = root.right
    #     return res
    #
    # def pre_sym_traverse(root):
    #     res = []
    #     s = []
    #     while root or s:
    #         while root:
    #             s.append(root)
    #             res.append(root.val)
    #             root = root.right
    #         if s:
    #             root = s.pop()
    #             root = root.left
    #     return res
    # return pre_traverse(root)

    # Solution3
    def is_symmetrical(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return is_symmetrical(root1.left, root2.right) and is_symmetrical(root1.right, root2.left)

    if not root:
        return True
    return is_symmetrical(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = layer2_left = TreeNode(4)
    root.right = layer2_right = TreeNode(4)
    layer2_left.right = layer3_left_left = TreeNode(6)
    layer2_left.left = layer3_left_right = TreeNode(3)
    layer2_right.right = layer3_right_left = TreeNode(3)
    layer2_right.left = layer3_right_right = TreeNode(6)

    print(symmetrical_tree(root))


