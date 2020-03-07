#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def layer_traverse(root):
    s = [root]
    res = []
    while s:
        root = s.pop(0)
        res.append(root.val)
        if root.left:
            s.append(root.left)
        if root.right:
            s.append(root.right)

    return res
    

class Solution(object):
    def get_tree_from_layer_traverse(self, nums):
        if not nums:
            return
        l = len(nums)
        index = 0
        res = []
        while index < l:
            if nums[index] != "null":
                cur_node = TreeNode(nums[index])
            else:
                cur_node = None

            print("index:", index)
            if index >= 1:
                parent_index = (index - 1) >> 1
                if index % 2 != 0:
                    res[parent_index].left = cur_node
                else:
                    res[parent_index].right = cur_node
            res.append(cur_node)
            index += 1
        
        return res[0] 
    

if __name__ == "__main__":
    nums = [1,4,4,"null",2,2,"null",1,"null",6,8,"null","null","null","null",1,3]
    # nums = [8, 8, 7, 9, 2, "null", "null", "null", "null", 4, 7]
    solu = Solution()
    root = solu.get_tree_from_layer_traverse(nums)
    print(layer_traverse(root))