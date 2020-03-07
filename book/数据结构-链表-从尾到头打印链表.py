#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.listNode import ListNode

def print_reverse_linked_list(root):
    """
    :param root: TreeNode
    :return: List[int]
    """
    stack = []
    while root:
        stack.append(root.val)
        root = root.next
    while stack:
        temp = stack.pop()
        print(temp)

    # if root.next:
    #     print_reverse_linked_list(root.next)
    # print(root.val)

if __name__ =="__main__":
    head = ListNode(1)
    head_2 = ListNode(2)
    head_3 = ListNode(3)
    head_4 = ListNode(4)
    head_5 = ListNode(5)
    head.next = head_2
    head_2.next = head_3
    head_3.next = head_4
    head_4.next = head_5
    head_5.next = None

    print_reverse_linked_list(head)